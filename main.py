import cv2
import numpy as np
import dlib

# Константы
width = 600
height = 400

# Подключение детектора, настроенного на поиск человеческих лиц
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture('video/My_video.mp4')
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
        # Выводим количество лиц на изображении
        if len(faces) > 1:
            print("Много людей в кадре!")
        elif len(faces) == 0:
            print("Невозможно разобрать лицо!")

        # Получение координат вершин прямоугольника и его построение на изображении
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        cv2.line(frame, (x1, y1 - 10), (x2, y1 - 10), (255, 0, 0), 1)

        if y1 < height * 0.1 or x1 < width * 0.25 or x2 > width * 0.75:
            print("Плохо!")

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

# # Получение координат контрольных точек и их построение на изображении
# landmarks = predictor(img, face)
# for n in range(0, 68):
#     x = landmarks.part(n).x
#     y = landmarks.part(n).y
#     cv2.circle(img, (x, y), 3, (255, 0, 0), -1)


# cv2.putText(img, "Press ESC to close frame", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Вывод преобразованного изображения
