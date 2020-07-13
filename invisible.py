#!/usr/bin/env python3
import cv2
import numpy as np

cap=cv2.VideoCapture(0)
back=cv2.imread('./image.jpeg')

while cap.isOpened():
    ret,frame=cap.read()

    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv",hsv)
        blue=np.uint8([[[255,0,0]]])
        blue_hsv=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
        # print(blue_hsv)

        l_blue=np.array([110,50,50])
        h_blue=np.array([130,255,255])
        mask=cv2.inRange(hsv,l_blue,h_blue)
        # cv2.imshow("mask",mask)

        part1=cv2.bitwise_and(back,back,mask=mask)
        # cv2.imshow("part1",part1)

        mask=cv2.bitwise_not(mask)

        part2=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("mask",part1+part2)

        if cv2.waitKey(5)==ord('q'):
            #save the image
            # cv2.imwrite('image.jpeg',back)
            break

cap.release()
cv2.destroyAllWindows()
