import dlib
import mediapipe as mp
import cv2
import numpy as np
import time
import utils.fps_util as fps_util

fps_util = fps_util.fps_util()

# dlib
dlib_detector = dlib.get_frontal_face_detector()
dlib_predictor = dlib.shape_predictor("./dat/shape_predictor_68_face_landmarks.dat")

# mediapipe
mp_pose = mp.solutions.pose

# webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

while webcam.isOpened():
    status, frame = webcam.read()

    fps_util.print_fps()

    # face detection using dlib and draw rectangle
    



    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
