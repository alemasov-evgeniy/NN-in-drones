# from djitellopy import Tello
# import cv2
# import time
#
# # Инициализация дрона и подключения к видеопотоку
# fly = Tello()
# fly.connect()
# print(fly.get_temperature())
# print(fly.get_battery())
#
# # Включение видеопотока
# fly.streamon()
#
# # Инициализация каскада для распознавания лиц
# faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# # Переменные
# faceCount = 0  # Текущее количество найденных лиц
# maxFaces = 0  # Максимальное количество посчитанных лиц
#
# # Взлет
# fly.takeoff()
# time.sleep(2)  # Небольшая задержка для стабилизации дрона
#
# # Подъем на 120 см
# fly.move_up(50)
# time.sleep(2)
#
# # Подсчет лиц в кадре
# while True:
#     # Получение текущего кадра с камеры дрона
#     frame = fly.get_frame_read().frame
#
#     if frame is None:
#         print("Не удалось получить кадр с камеры")
#         continue
#
#     # Преобразование кадра в оттенки серого для распознавания лиц
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Поиск лиц на кадре с использованием каскада лиц
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=2,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#
#     faceCount = len(faces)  # Текущее количество найденных лиц
#
#     if maxFaces == faceCount and faceCount != 0:
#         # Если количество лиц не изменилось и найдено хотя бы одно лицо
#         print('Окончательный счет: ' + str(maxFaces))
#         fly.land()  # Посадка дрона
#         break
#     elif maxFaces < faceCount:
#         # Если распознано больше лиц
#         print(f'Найдено больше лиц: {faceCount - maxFaces}')
#         maxFaces = faceCount  # Обновление максимального количества найденных лиц
#
#         # Перемещение назад для поиска новых лиц
#         fly.move_back(20)
#         time.sleep(4)
#
#     # Отображение видео с распознанными лицами
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Отображение видеопотока на экране
#     cv2.imshow('Drone Camera', frame)
#
#     # Прерывание цикла, если нажата клавиша 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         fly.streamoff()
#         cv2.destroyAllWindows()
#         fly.end()
#         break
#
# # Остановка видеопотока и завершение работы
# fly.streamoff()
# cv2.destroyAllWindows()
# fly.end()

# from djitellopy import Tello
# import cv2
# import time
#
# # Инициализация дрона и подключения к видеопотоку
# fly = Tello()
# fly.connect()
# print(f"Температура дрона: {fly.get_temperature()} °C")
# print(f"Заряд батареи: {fly.get_battery()} %")
#
# # Включение видеопотока
# fly.streamon()
#
# # Инициализация каскада для распознавания лиц
# faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#
# # Переменные
# total_faces = 0  # Общее количество найденных лиц
#
# # Взлет дрона
# fly.takeoff()
# time.sleep(2)  # Небольшая задержка для стабилизации дрона
#
# # Подъем на 50 см
# # fly.move_up(50)
# # time.sleep(2)
#
# # Дрон должен обследовать несколько позиций
# positions = 2  # Количество позиций, которые дрон облетит
#
# for position in range(positions):
#     # Получение текущего кадра с камеры дрона
#     frame = fly.get_frame_read().frame
#
#     if frame is None:
#         print("Не удалось получить кадр с камеры")
#         continue
#
#     # Преобразование кадра в оттенки серого для распознавания лиц
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Поиск лиц на кадре с использованием каскада лиц
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30),
#         flags=cv2.CASCADE_SCALE_IMAGE
#     )
#
#     # Добавляем количество лиц, найденных на текущем кадре, к общему счету
#     face_count = len(faces)
#     total_faces += face_count
#
#     print(f"На позиции {position + 1} найдено лиц: {face_count}")
#
#     # Отображение видео с распознанными лицами
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Отображение видеопотока на экране
#     cv2.imshow('Drone Camera', frame)
#
#     # Дрон перемещается вправо для поиска следующей картины
#     fly.move_right(25)
#     time.sleep(2)  # Задержка, чтобы дрон успел переместиться
#
#     # Прерывание цикла, если нажата клавиша 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Завершение миссии: посадка и вывод результатов
# fly.land()
# print(f"Всего найдено лиц: {total_faces}")
#
# # Остановка видеопотока и завершение работы
# fly.streamoff()
# cv2.destroyAllWindows()
# fly.end()



from djitellopy import Tello
import cv2
import time
import numpy as np

# Инициализация дрона и подключения к видеопотоку
fly = Tello()
fly.connect()
print(fly.get_temperature())
print(fly.get_battery())

# Включение видеопотока
fly.streamon()

# Инициализация каскада для распознавания лиц
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Переменные
unique_faces = []  # Список для хранения уникальных лиц

# Взлет
fly.takeoff()
time.sleep(2)  # Небольшая задержка для стабилизации дрона

# Подсчет лиц в кадре
start_time = time.time()
while time.time() - start_time < 7:  # Смотрим 7 секунд
    # Получение текущего кадра с камеры дрона
    frame = fly.get_frame_read().frame

    if frame is None:
        print("Не удалось получить кадр с камеры")
        continue

    # Преобразование кадра в оттенки серого для распознавания лиц
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Поиск лиц на кадре с использованием каскада лиц
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100),  # Минимальный размер лица
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Проверка найденных лиц на уникальность
    for (x, y, w, h) in faces:
        # Находим центр лица
        center_face = (x + w // 2, y + h // 2)

        # Проверяем, не слишком ли близко к уже найденным лицам
        is_unique = True
        for (ux, uy, uw, uh) in unique_faces:
            center_unique = (ux + uw // 2, uy + uh // 2)
            distance = np.linalg.norm(np.array(center_face) - np.array(center_unique))  # Расстояние между центрами

            # Если расстояние меньше 50 пикселей, считаем это одно и то же лицо
            if distance < 50:
                is_unique = False
                break

        # Если лицо уникально, добавляем его в список
        if is_unique:
            unique_faces.append((x, y, w, h))
            # Рисование прямоугольников на лицах
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Отображение видеопотока на экране
    cv2.imshow('Drone Camera', frame)

    # Прерывание цикла, если нажата клавиша 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Посадка дрона
fly.streamoff()
fly.land()


# Подсчет уникальных лиц
faceCount = len(unique_faces)

# Создание окна с результатами
result_window = frame.copy()  # Создаем новое окно с последним кадром

# Рисуем прямоугольники на уникальных лицах на итоговом изображении
for (x, y, w, h) in unique_faces:
    cv2.rectangle(result_window, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Добавляем текст с количеством найденных лиц
cv2.putText(result_window, f'Faces found: {faceCount}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)
cv2.imshow('Result', result_window)

# Вывод количества найденных лиц в консоль
print(f'Number of unique faces found: {faceCount}')

# Ожидание закрытия окна результатов
cv2.waitKey(0)
cv2.destroyAllWindows()
fly.end()











