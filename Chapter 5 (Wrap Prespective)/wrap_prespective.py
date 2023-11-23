'''
This code will put warp perspective on an imge to get its bird eye view (top view)
'''
import cv2
import numpy as np

img = cv2.imread("cards.png")

# To get warp perspective of an image we need its four cornor point, use ms paint to get thoes points
# Function below declears points as a numpy array of floats
p1 = np.float32([[428,20],[500,174],[214,119],[284,272]])

# define width and height of normal playing card
width, height = 250,350

# defines which point refers to which corner
p2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Function gets transformation matrix for the warp prespective
matrix = cv2.getPerspectiveTransform(p1,p2)

# Funciton gets output wrap prespective image based on the above matrix defined
# takes source image, matrix and width & height as arguments
imgOut = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("image", img)
cv2.imshow("image", imgOut)
cv2.waitKey(0)
