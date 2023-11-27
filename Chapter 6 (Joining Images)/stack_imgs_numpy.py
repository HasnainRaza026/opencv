'''Joining Multiple Images
This code will display multiple imges in a single window'''

import cv2
import numpy as np

img = cv2.imread("image.png")


# np.hstack function stacks the images in horizontal
# takes one positional argument, a tuple containing images
imgHor = np.hstack((img,img))

# np.vstack function stacks the images in vertical
# takes one positional argument, a tuple containing images
imgVer = np.vstack((img,img))

cv2.imshow('window1', imgHor)

cv2.imshow('window2', imgVer)

cv2.waitKey(0)


# This method of stacking images using numpy has fwe issues
# 1. We can't resize the images, they will display aas it is
# 2. It does not support different channel images
# to overcome this problem use external function
