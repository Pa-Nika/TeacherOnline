import cv2
import dlib
import pandas as pd
from visualization import graph

# Константы
width = 330
height = 220


class PositionAnalysis(object):
    def __init__(self, path):
        # Подключение детектора, настроенного на поиск человеческих лиц
        self.df_diff = None
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        self.loading_dialog = None
        self.pixmap = None
        self.path = path
        self.df = None
        self.flag_is_stop_pressed = True

    def set_loading_dialog(self, loading):
        self.loading_dialog = loading

    def set_flag_is_stop_pressed(self):
        self.flag_is_stop_pressed = False

    def csv_creator(self):
        points = ['left_x', 'left_y', 'up_x', 'up_y', 'right_x', 'right_y', 'lower_x', 'lower_y']
        difference = ['left', 'up', 'right', 'lower', 'max']
        self.df = pd.DataFrame(columns=points)
        self.df_diff = pd.DataFrame(columns=difference)

    def work(self):
        self.csv_creator()

        cap = cv2.VideoCapture(self.path)
        frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        count_for_one_percent = round(frame_number / 100) - 1
        count_frame_in_while = 0

        # and self.flag_is_stop_pressed is True

        while cap.isOpened():

            flag, frame = cap.read()
            if not flag:
                break

            dim = (width, height)
            frame = cv2.resize(frame, dim)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Проверяем количество лиц на изображении
            faces = self.detector(gray)
            if len(faces) > 1:
                # self.textEdit.setText("Много людей в кадре!")
                flag = False
            elif len(faces) == 0:
                # self.textEdit.setText("Невозможно разобрать лицо!")
                flag = False

            for face in faces:
                if not flag:
                    flag = True
                    continue

                # Получение координат контрольных точек и их построение на изображении
                landmarks = self.predictor(gray, face)

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

                left_square = ((round(width / 3) - x_0) / 10) ** 2
                right_square = ((round(width * 2 / 3) - x_16) / 10) ** 2
                up_square = ((round(height * 0.09) - y_27) / 10) ** 2
                lower_square = ((round(height * 0.7) - y_9) / 10) ** 2
                max_square = max(left_square, right_square, up_square, lower_square)

                self.df.loc[len(self.df.index)] = [x_0, y_0, x_27, y_27, x_16, y_16, x_9, y_9]
                self.df_diff.loc[len(self.df_diff.index)] = [left_square, up_square, right_square, lower_square, max_square]

                # if y_9 > height * 0.75:
                #     self.textEdit.setText("Голова слишком низко")
                # elif y_27 < height * 0.25:
                #     self.textEdit.setText("Голова слишком высоко")
                # elif x_0 < width * 0.25:
                #     self.textEdit.setText("Голова слишком слева")
                # elif x_16 > width * 0.75:
                #     self.textEdit.setText("Голова слишком справа")
                # elif abs(x_27 - x_0) < width * 0.05:
                #     self.textEdit.setText("Голова повернута влево")
                # elif abs(x_27 - x_16) < width * 0.05:
                #     self.textEdit.setText("Голова повернута вправо")
                # else:
                #     self.textEdit.setText("Все хорошо!")
            count_frame_in_while += 1
            if count_frame_in_while == count_for_one_percent:
                self.loading_dialog.my_event()
                count_frame_in_while = 0

            cv2.imwrite('cam.png', frame)
            # self.loading_dialog.set_frame('cam.png')
            key = cv2.waitKey(2)
            if key == 27 or self.loading_dialog is None:
                # self.work_window.close()
                break

        cap.release()
        cv2.destroyAllWindows()
        # if self.flag_is_stop_pressed is True:
        self.df.to_csv(r'my_data.csv', index=False)
        self.df_diff.to_csv(r'square_diff.csv', index=False)
        obj_graph = graph.Graph(self.df_diff)
