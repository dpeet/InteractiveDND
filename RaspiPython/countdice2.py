# -*- coding: utf-8 -*-

'''
This script uses OpenCV 2.3.1 or greater to examine a webcam image for white dice with black pips being thrown into a brown box.
www.hehoe.de
'''

import numpy
import cv2
import sys

HAVE_DISPLAY = True  # show debug windows

BINARIZATION_THRESHOLD = 60  # Selects the bright white die area

# Area size definitions (the script "knows" how big a die should be)
AREA_FACTOR = 1  # compensate camera zoom or position
DIE_AREA_MIN = AREA_FACTOR * 1400
DIE_AREA_MAX = AREA_FACTOR * 1700
PIP_AREA_MIN = AREA_FACTOR * 45
PIP_AREA_MAX = AREA_FACTOR * 70

# vc = cv2.VideoCapture()  # prepare webcam for input
# vc.open(0)  # open webcam
if not True:
    print ("Could not open camera.")
    sys.exit(1)
else:
    # higher resolutions do not work on the raspberry pi for USB-Webcams with uncompressed video
    # see http://www.raspberrypi.org/phpBB3/viewtopic.php?f=37&t=11745&p=135060#p135060
    # vc.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 960)
    # vc.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 720)

    # tweak record properties for different lighting
    # the semantics of these commands are dependant on opencv version, os and camera driver.
    # sometimes the values are float, sometimes integer.

    # atom, windows
    # vc.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS,0.5)
    # vc.set(cv2.cv.CV_CAP_PROP_CONTRAST,0.125)

    # pi, debian
    # vc.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS,0.6)
    # vc.set(cv2.cv.CV_CAP_PROP_CONTRAST,0.130)
    # vc.set(cv2.cv.CV_CAP_PROP_SATURATION,0.130)
    # vc.set(cv2.cv.CV_CAP_PROP_GAIN,0.08)

    dilateKernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
    # while True:
    # retval, image = vc.read()  # read frame from camera
    image = cv2.imread("image6.jpg")
    if not True:
        print ("Could not read frame from camera.")
        sys.exit(1)
    else:
        # cv2.imshow('input', image)
        image = image[60:-60, 40:-50]  # crop picture
        # cv2.imshow('cropped', image)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # convert to grayscale
        retval, bin = cv2.threshold(gray, BINARIZATION_THRESHOLD, 255, cv2.THRESH_BINARY)  # select white die areas
        bin = cv2.dilate(bin, dilateKernel)  # dilate white areas to prevent pip fraying
        if HAVE_DISPLAY:
            cv2.imshow('binary', bin)
        im3, contours0, hierarchy = cv2.findContours(bin.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find contours
        contours = [cv2.approxPolyDP(cnt, 2, True) for cnt in contours0]  # simplify contours

        # for all contours: check white area size (die), check area size of sub-contours (pips)
        dice = []
        for i in range(len(contours)):
            dieCnt = contours[i]
            dieArea = cv2.contourArea(dieCnt)
            print (i, " ", dieArea)

            if dieArea > DIE_AREA_MIN and dieArea < DIE_AREA_MAX:
                # print "Contour", i, "is a die with area", dieArea
                pipId = hierarchy[0][i][2]
                pipContours = []
                while not pipId == -1:
                    pipCnt = contours[pipId]
                    pipArea = cv2.contourArea(pipCnt)
                    if pipArea > PIP_AREA_MIN and pipArea < PIP_AREA_MAX:
                        # print "Contour", i, "is a pip with area", pipArea
                        pipContours.append(pipCnt)
                        # else:
                        # print "Pip",pipId,"with area",pipArea,"discarded"
                    pipId = hierarchy[0][pipId][0]
                dice.append((dieCnt, pipContours))
                # else:
                # print "Contour",i,"with area",dieArea,"discarded"

        sum = 0
        for i in range(len(dice)):
            dieCnt, pipContours = dice[i]
            cv2.drawContours(image, [dieCnt], -1, (64, 64, 128), 2)
            cv2.drawContours(image, pipContours, -1, (64, 128, 64), 2)
            sum = sum + len(pipContours)
            cv2.putText(image, "%d" % len(pipContours), (dieCnt[0][0][0], dieCnt[0][0][1]), cv2.FONT_HERSHEY_PLAIN,
                        2.0, (255, 64, 64), 2)
        cv2.putText(image, "%d" % sum, (10, 50), cv2.FONT_HERSHEY_PLAIN, 3.0, (255, 255, 255), 2)
        cv2.imshow('Die and Pips', image)

        if HAVE_DISPLAY:
            ch = cv2.waitKey(0)
            # if ch == 27:  # exit on Esc
            #     break
