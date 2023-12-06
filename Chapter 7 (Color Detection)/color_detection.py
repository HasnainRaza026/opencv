'''Color Detection
This code will detect the color of the image and will display
only that specific colored poortion'''

import cv2
import numpy as np


def empty(h):
    pass

# An external function to stack multiple images, 
# its also allows to resize the images and allows different chennel images
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


# Creating & resizing the trackbar window
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)

# adding trackbars to the window
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty) # function takes name, window, minimum value and maximum value, and a functioon
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

while True:
    img =cv2.imread("image2.png")

    # Getting trackbar values and storing them in a variable
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    print(h_min,h_max,s_min,s_max,v_min,v_max)


    '''The HSV (which stands for Hue Saturation Value) 
    scale provides a numerical readout of your image that 
    corresponds to the color names contained therein.

    Hue ---> Hues are the three primary colors (red, blue, and yellow) 
            and the three secondary colors (orange, green, and violet)

    Saturation ---> Color saturation is the purity and intensity of a color as displayed in an image.

    Value ---> Color value refers to the relative lightness or darkness of a color.'''
    # Converting image into HSV image
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



    # storing max and min hsv values in a numpy array
    lower, upper = np.array([h_min, s_min, v_min]), np.array([h_max, s_max, v_max])

    # creating mask (a filtered out image in the defined value ranges)
    # returns exact location of pixels contain the required information (color)
    mask = cv2.inRange(img_hsv,lower,upper)

    # Creating a new image (final output) by adding mask and original image togeather
    img_res = cv2.bitwise_and(img, img, mask=mask)


    img_stack = stackImages(0.4, ([img,img_hsv], [mask,img_res]))
    cv2.imshow("Result", img_stack)
    cv2.waitKey(1)
