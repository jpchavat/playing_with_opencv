__author__ = 'jpchavat'

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
    _threshold = 25
    print "Threshold: ", _threshold

    # Times to skip taking a new background sample
    times_skip_sample = 5
    times = times_skip_sample

    font = cv2.FONT_HERSHEY_SIMPLEX

    ret, last = cap.read()
    last1 = cv2.cvtColor(last, cv2.cv.CV_BGR2GRAY)
    last2 = last1.copy()

    _time = time.time()
    _fps = ""

    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)
        if ret is True:
            to_show = np.array(np.where(abs(last1 - frame) > _threshold,
                                        255, 0), dtype=np.uint8)

        if times == times_skip_sample:
            last1 = (last2 * 0.1 + last1 * 0.2 + frame * 0.7)  # average
            last2 = last1.copy()
            time_aux = time.time()
            _fps = "%.2f" % (times / (time_aux - _time))
            _time = time_aux
            times = 0
        else:
            times += 1

        cv2.putText(to_show, 'FPS: ' + _fps, (40, 40), font, 1,
                    (255, 255, 0), 2)

        cv2.imshow('frame', to_show)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    doTheThing()
