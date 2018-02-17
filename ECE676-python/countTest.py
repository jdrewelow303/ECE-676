import cv2
import numpy as np

vc = cv2.VideoCapture(1)
i=0

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:


    frame2 = cv2.Canny(cv2.blur(frame,(3,3)),150,200)
    (flag, contours, h) = cv2.findContours(frame2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow("Test2", frame2)
    #cv2.imshow("Test", frame)
    #frame = cv2.drawContours(frame,contours,0,(0,250,0),3)
    #frame = cv2.fillPoly(frame, contours, (0, 0, 0))
    #a = cv2.pointPolygonTest(contours[0],(233,290),False)
    #print (contours[0])
    #cv2.imshow("a", frame)

    if len(contours) != 0:
        rect = cv2.boundingRect(contours[0])
        if (rect[2] + rect[3]) < 148:
            print("skittle")
        else:
            print("M&M")
        cv2.imshow("Test", cv2.rectangle(frame,(rect[0],rect[1]),((rect[0]+rect[2]),(rect[1]+rect[3])),250))
    else:
        cv2.imshow("Test", frame)

    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()
