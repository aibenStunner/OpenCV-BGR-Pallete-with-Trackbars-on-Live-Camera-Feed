__author__ = '8.Ball'

import cv2
import numpy as np

def doNothing(x):
    pass

windowName = 'Life Feed'
cap = cv2.VideoCapture(0)
cv2.namedWindow(windowName)
# thresh = 40

cv2.createTrackbar('Blue', windowName, 0, 255, doNothing)
cv2.createTrackbar('Green', windowName, 0, 255, doNothing)
cv2.createTrackbar('Red', windowName, 0, 255, doNothing)
cv2.createTrackbar('Threshold', windowName, 0, 100, doNothing)

while True:
    ret, frame = cap.read()

    #Get Trackbar positions
    B = cv2.getTrackbarPos('Blue', windowName)
    G = cv2.getTrackbarPos('Green', windowName)
    R = cv2.getTrackbarPos('Red', windowName)
    thresh = cv2.getTrackbarPos('Threshold', windowName)
    bgrTrack = [B, G, R]

    hsvTrack = cv2.cvtColor(np.uint8([[bgrTrack]] ), cv2.COLOR_BGR2HSV)[0][0]


    minHSVTrack = np.array([hsvTrack[0] - thresh, hsvTrack[1] - thresh, hsvTrack[2] - thresh])
    maxHSVTrack = np.array([hsvTrack[0] + thresh, hsvTrack[1] + thresh, hsvTrack[2] + thresh])
    # print(minHSVTrack)
    hsvFeed = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    imageMask = cv2.inRange(hsvFeed, minHSVTrack, maxHSVTrack)
    outputColor = cv2.bitwise_and(frame, frame, mask = imageMask)

    cv2.imshow(windowName, frame)
    cv2.imshow('Image Mask Feed', imageMask)
    cv2.imshow('Color only Feed', outputColor)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()