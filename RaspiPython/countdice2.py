# -*- coding: utf-8 -*-

'''
This script uses OpenCV 2.3.1 or greater to examine a webcam image for white dice with black pips being thrown into a brown box.
www.hehoe.de
'''

import numpy
import cv2
import sys

HAVE_DISPLAY = True  # show debug windows

BINARIZATION_THRESHOLD = 50  # Selects the bright white die area

# Area size definitions (the script "knows" how big a die should be)
AREA_FACTOR = 1  # compensate camera zoom or position
DIE_AREA_MIN = AREA_FACTOR * 1000
DIE_AREA_MAX = AREA_FACTOR * 3000
PIP_AREA_MIN = AREA_FACTOR * 5
PIP_AREA_MAX = AREA_FACTOR * 30



def get_num_from_dice():
    # retval, image = vc.read()  # read frame from camera
    image = cv2.imread("image7.jpg")
    # cv2.imshow('input', image)
    image = image[0:-200, 300:-100]  # crop picture
    # cv2.imshow('cropped', image)
    # image = cv2.medianBlur(image, 5)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # convert to grayscale
    retval, bin = cv2.threshold(gray, BINARIZATION_THRESHOLD, 255, cv2.THRESH_BINARY)  # select white die areas
    dilateKernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (7, 7))
    bin = cv2.dilate(bin, dilateKernel)  # dilate white areas to prevent pip fraying
    cv2.imshow("dilated", bin)
    if HAVE_DISPLAY:
        cv2.imshow('binary', bin)
    _, contours0, hierarchy = cv2.findContours(bin.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # find contours
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

    die_sum = 0
    dice_numbers = []
    for i in range(len(dice)):
        dieCnt, pipContours = dice[i]
        cv2.drawContours(image, [dieCnt], -1, (64, 64, 128), 2)
        cv2.drawContours(image, pipContours, -1, (64, 128, 64), 2)
        dice_numbers.append(len(pipContours))
        die_sum = die_sum + len(pipContours)
        cv2.putText(image, "%d" % len(pipContours), (dieCnt[0][0][0], dieCnt[0][0][1]), cv2.FONT_HERSHEY_PLAIN,
                    2.0, (255, 64, 64), 2)
    cv2.putText(image, "%d" % die_sum, (10, 50), cv2.FONT_HERSHEY_PLAIN, 3.0, (255, 255, 255), 2)
    cv2.imshow('Die and Pips', image)

    if HAVE_DISPLAY:
        ch = cv2.waitKey(0)
        # if ch == 27:  # exit on Esc
        #     break
    return die_sum

get_num_from_dice()