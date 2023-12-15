'''
This code will extract colors (Red, Green, Blue, Orange, White, Yellow)
from the rubicks cube and displays their mask
'''

import cv2
import numpy as np

# Function to stack multiple images/videos
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

cap = cv2.VideoCapture(1)

while True:
    rate, frame = cap.read()
    img_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Calebrated HSV values for red color
    lower_Red = np.array([158,0,156])
    upper_Red = np.array([179,230,255])
    # Generating mask for red color
    mask_Red = cv2.inRange(img_HSV, lower_Red, upper_Red)

    # Calebrated HSV values for green color
    lower_Greean = np.array([64,97,150])
    upper_Greean = np.array([70,255,255])
    # Generating mask for green color
    mask_Green = cv2.inRange(img_HSV, lower_Greean, upper_Greean)

    # Calebrated HSV values for blue color
    lower_Blue = np.array([95,216,185])
    upper_Blue = np.array([100,255,253])
    # Generating mask for blue color
    mask_Blue = cv2.inRange(img_HSV, lower_Blue,upper_Blue)

    # Calebrated HSV values for orange color
    lower_Orange = np.array([4,176,188])
    upper_Orange = np.array([6,213,229])
    # Generating mask for orange color
    mask_Orange = cv2.inRange(img_HSV, lower_Orange,upper_Orange)

    # Calebrated HSV values for yellow color
    lower_Yellow = np.array([29,186,159])
    upper_Yellow = np.array([38,228,188])
    # Generating mask for yellow color
    mask_Yellow = cv2.inRange(img_HSV, lower_Yellow,upper_Yellow)

    # Calebrated HSV values for white color
    lower_White = np.array([99,23,172])
    upper_White  = np.array([113,54,198])
    # Generating mask for white color
    mask_White  = cv2.inRange(img_HSV, lower_White,upper_White)

    # Generating colored mask by combining mask with actual frame
    img_red = cv2.bitwise_and(frame, frame, mask=mask_Red)
    img_green = cv2.bitwise_and(frame, frame, mask=mask_Green)
    img_blue = cv2.bitwise_and(frame, frame, mask=mask_Blue)
    img_orange = cv2.bitwise_and(frame, frame, mask=mask_Orange)
    img_yellow = cv2.bitwise_and(frame, frame, mask=mask_Yellow)
    img_white = cv2.bitwise_and(frame, frame, mask=mask_White)

    img_stack = stackImages(0.3, ([frame, img_red], [img_green, img_blue], [img_orange, img_yellow], [img_white, frame]))
    cv2.imshow("out1", img_stack)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
