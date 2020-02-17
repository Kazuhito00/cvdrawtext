#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2 as cv

from cvdrawtext import CvDrawText


def main():
    cv_image = cv.imread("image/sample.png")

    font_path = './font/x12y20pxScanLine.ttf'

    image = CvDrawText.puttext(cv_image, u"TEST", (30, 30), font_path, 60,
                               (255, 255, 255))  # RGB

    cv.imshow("sample", image)
    cv.waitKey(0)


if __name__ == '__main__':
    main()
