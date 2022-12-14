import cv2
import dlib
from PyQt5.uic.properties import QtGui

# Константы
width = 330
height = 220


class PositionAnalysis(object):
    def __init__(self, path, text_edit, frame):
        self.workWindow = None
        self.pixmap = None
        self.path = path
        self.textEdit = text_edit
        self.frameWindow = frame

    def set_work_window(self, window):
        self.workWindow = window

    def work(self):
        flag = True

        # Подключение детектора, настроенного на поиск человеческих лиц
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        cap = cv2.VideoCapture(self.path)

        while cap.isOpened():
            flag, frame = cap.read()

            if not flag:
                break

            dim = (width, height)
            frame = cv2.resize(frame, dim)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Проверяем количество лиц на изображении
            faces = detector(gray)
            if len(faces) > 1:
                self.textEdit.setText("Много людей в кадре!")
                flag = False
            elif len(faces) == 0:
                self.textEdit.setText("Невозможно разобрать лицо!")
                flag = False

            for face in faces:
                if not flag:
                    flag = True
                    continue

                # Получение координат контрольных точек и их построение на изображении
                landmarks = predictor(gray, face)

                # нижняя точка
                x_9 = landmarks.part(8).x
                y_9 = landmarks.part(8).y
                cv2.circle(frame, (x_9, y_9), 3, (255, 0, 0), -1)

                # Точка между глазами
                x_27 = landmarks.part(27).x
                y_27 = landmarks.part(27).y
                cv2.circle(frame, (x_27, y_27), 3, (255, 0, 0), -1)

                # Левая точка
                x_0 = landmarks.part(0).x
                y_0 = landmarks.part(0).y
                cv2.circle(frame, (x_0, y_0), 3, (255, 0, 0), -1)

                # Правая точка
                x_16 = landmarks.part(16).x
                y_16 = landmarks.part(16).y
                cv2.circle(frame, (x_16, y_16), 3, (255, 0, 0), -1)

                if y_9 > height * 0.75:
                    self.textEdit.setText("Голова слишком низко")
                elif y_27 < height * 0.25:
                    self.textEdit.setText("Голова слишком высоко")
                elif x_0 < width * 0.25:
                    self.textEdit.setText("Голова слишком слева")
                elif x_16 > width * 0.75:
                    self.textEdit.setText("Голова слишком справа")
                elif abs(x_27 - x_0) < width * 0.05:
                    self.textEdit.setText("Голова повернута влево")
                elif abs(x_27 - x_16) < width * 0.05:
                    self.textEdit.setText("Голова повернута вправо")
                else:
                    self.textEdit.setText("Все хорошо!")

            # self.pixmap = QtGui.QPixmap('background2.png')
            # self.frameWindow.setPixmap(self.pixmap)
            cv2.imwrite('cam.png', frame)
            self.workWindow.set_frame('cam.png')

            # cv2.imshow("Frame", frame)
            key = cv2.waitKey(2)
            if key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

