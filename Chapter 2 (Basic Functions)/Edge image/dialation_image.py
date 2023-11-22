'''
Sometimes an edge is not detected as a line (due to gap or improper joints)
to counter this error we can increase the thickness of the edges'''

import cv2
import numpy as np

# Define a kernal using numpy
# np.ones() --> make all the values to be one, takes two argumentz the size of matrix, the type of object
# np.uint8() --> the object is unsigned integer of 8 bits
kernal = np.ones((5,5), np.uint8())

img = cv2.imread("image.png")

imgEdge = cv2.Canny(img, 100, 100)

# Function increase the thickness of the edge, takes 3 arguments, a canny image,
# a kernal (a matrix having size and value), and the thicness
imgThick = cv2.dilate(imgEdge, kernal, iterations=1 )

cv2.imshow("edge image", imgThick)
cv2.waitKey(0)
