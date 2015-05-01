__author__ = 'jp'

import numpy as np
import cv2

import time


def doTheThing():

    # Instance of VideoCapture to capture webcam(0) images
    cap = cv2.VideoCapture(0)
    cap.open(0)

    # Getting width and height of captured images
    w = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    print "Width: ", w, "Height: ", h

    # Threshold to consider a difference as a difference (u know what I mean)
    _threshold = 100
    print "Threshold: ", _threshold

    ret, last = cap.read()
    last = cv2.cvtColor(last, cv2.cv.CV_BGR2GRAY)
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)
        if ret is True:
            to_show = np.array(np.where(abs(last - frame) > _threshold, 255, 0),
                               dtype=np.uint8)

            last = frame.copy()

        cv2.imshow('frame', to_show)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    doTheThing()
