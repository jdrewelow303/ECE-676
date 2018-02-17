import cv2
import numpy as np

showFrame = 'm'
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    lower_red = np.array([70, 0, 0])
    upper_red = np.array([100, 20, 20])
    redMask = cv2.inRange(rgb, lower_red, upper_red)

    lower_orange = np.array([140, 40, 0])
    upper_orange = np.array([180, 60, 20])
    orangeMask = cv2.inRange(rgb, lower_orange, upper_orange)

    lower_green = np.array([20, 50, 0])
    upper_green = np.array([40, 80, 20])
    greenMask = cv2.inRange(rgb, lower_green, upper_green)

    lower_yellow = np.array([130, 120, 0])
    upper_yellow = np.array([190, 150, 20])
    yellowMask = cv2.inRange(rgb, lower_yellow, upper_yellow)

    lower_purple = np.array([0, 0, 0])
    upper_purple = np.array([50, 50, 50])
    purpleMask = cv2.inRange(rgb, lower_purple, upper_purple)

    red = cv2.bitwise_and(frame, frame, mask=redMask)
    orange = cv2.bitwise_and(frame, frame, mask=orangeMask)
    green = cv2.bitwise_and(frame, frame, mask=greenMask)
    yellow = cv2.bitwise_and(frame, frame, mask=yellowMask)
    purple = cv2.bitwise_and(frame, frame, mask=purpleMask)
    if showFrame == 'r':
        cv2.imshow("Test", red)
    elif showFrame == 'o':
        cv2.imshow("Test", orange)
    elif showFrame == 'g':
        cv2.imshow("Test", green)
    elif showFrame == 'y':
        cv2.imshow("Test", yellow)
    elif showFrame == 'p':
        cv2.imshow("Test", purple)
    else:
        cv2.imshow("Test", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == ord('r'):
        showFrame = 'r'
    elif key == ord('o'):
        showFrame = 'o'
    elif key == ord('g'):
        showFrame = 'g'
    elif key == ord('y'):
        showFrame = 'y'
    elif key == ord('p'):
        showFrame = 'p'
    elif key == ord('a'):
        showFrame = 'a'
    elif key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()
