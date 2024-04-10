from threading import Thread
import cv2, time


class ThreadedCamera(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        # FPS = 1/X
        # X = desired FPS
        self.FPS = 1 / 60
        self.FPS_MS = int(self.FPS * 1000)

        # Start frame retrieval thread
        self.thread = Thread(target=self.update, args=())
        self.frame = None
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()
            time.sleep(self.FPS)

    def show_frame(self):
        if self.frame is None or self.frame.size == 0:
            # Handle empty frame
            return False, None
        else:
            resized_frame = cv2.resize(self.frame, (1080, 1080))
            return True, self.frame

