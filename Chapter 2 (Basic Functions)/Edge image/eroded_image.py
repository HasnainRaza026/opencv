'''
Sometimes we want to make the edges thinner, we do erossion for that
'''

import cv2
import numpy as np

kernal = np.ones((5,5), np.uint8())

img = cv2.imread("image.png")

imgEdge = cv2.Canny(img, 100, 100)

imgThick = cv2.dilate(imgEdge, kernal, iterations=1)

# Function decrease the thickness of the edge, takes 3 arguments, an image,
# a kernal (a matrix having size and value), and the amount of thin
imgEroded = cv2.erode(imgThick, kernal, iterations=1)

cv2.imshow("edge image", imgEroded)
cv2.waitKey(0)
