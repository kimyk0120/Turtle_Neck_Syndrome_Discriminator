import time

class fps_util:
    def __init__(self):
        self.prevTime = 0

    def print_fps(self):
        curTime = time.time()
        sec = curTime - self.prevTime
        self.prevTime = curTime

        fps = 1 / (sec)
        print("FPS: %0.1f" % fps)

    def get_fps(self):
        curTime = time.time()
        sec = curTime - self.prevTime
        self.prevTime = curTime

        fps = 1 / (sec)
        return fps