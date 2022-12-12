import cv2
import dlib

# Константы
width = 600
height = 400


class PositionAnalysis(object):
    def __init__(self, path):
        self.path = path

    def work(self):
        # Подключение детектора, настроенного на поиск человеческих лиц
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

        cap = cv2.VideoCapture(self.path)
        # cap = cv2.VideoCapture('video/Test_video.mp4')

        while cap.isOpened():
            flag, frame = cap.read()
            # Изменяем размер кадра
            if not flag:
                break

            dim = (width, height)
            frame = cv2.resize(frame, dim)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)

            for face in faces:
                # Проверяем количество лиц на изображении
                if len(faces) > 1:
                    print("Много людей в кадре!")
                elif len(faces) == 0:
                    print("Невозможно разобрать лицо!")

                # Получение координат вершин прямоугольника и его построение на изображении
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                cv2.line(frame, (x1, y1 - 10), (x2, y1 - 10), (255, 0, 0), 1)

                if y1 < height * 0.1 or x1 < width * 0.25 or x2 > width * 0.75 or y1 > height * 0.25:
                    print("Плохо!")

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break

        cap.release()
        cv2.destroyAllWindows()