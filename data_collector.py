import dlib
import mediapipe
import cv2
import numpy as np
import time

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./dat/shape_predictor_68_face_landmarks.dat")


webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

prevTime = 0
while webcam.isOpened():
    status, frame = webcam.read()

    curTime = time.time()
    sec = curTime - prevTime
    prevTime = curTime

    fps = 1 / (sec)
    print("FPS: %0.1f" % fps)

    if status:

        # cv2.imshow("test", frame)

        pass


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

