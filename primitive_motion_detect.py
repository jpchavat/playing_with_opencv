__author__ = 'jp'

import numpy as np
import cv2

import time


def doTheThing():

    cap = cv2.VideoCapture(0)
    cap.open(0)
    w = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    threshold = 25

    print w, h

    ret, last = cap.read()
    while cap.isOpened():
        ret, frame = cap.read()
        toShow = np.zeros((h,w), dtype=np.uint8)
        if ret is True:
            for i in range(h):
                for j in range(w):
                    p0 = last.item(i, j, 0)
                    p00 = frame.item(i, j, 0)

                    if p0 - threshold > p00 or p00 > p0 + threshold:
                        p1 = last.item(i, j, 1)
                        p11 = frame.item(i, j, 1)
                        if p1 - threshold > p11 or p11 > p1 + threshold:
                            p2 = last.item(i, j, 2)
                            p22 = frame.item(i, j, 2)
                            if p2 - threshold > p22 or p22 > p2 + threshold:
                                toShow[i, j] = 255

            cv2.imshow('frame', toShow)

            last = frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)


if __name__ == '__main__':
    doTheThing()

