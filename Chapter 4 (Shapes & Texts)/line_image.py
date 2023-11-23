'''
This code will create a colored line in an image
'''
import cv2
import numpy as np

# Function creates matrix filled with zeros (A black image),
# takes pixels and number of chennels (an optional argument for colored image) as an argument
# zeros --> Black
# ones --> White
img = np.zeros((512,512,3),np.uint8)

# Function creates a green diagonal line starting from origin and ends at (300,300)
# this function takes image, starting and ending points, color of the line and thckness (optional) as arguments
#cv2.line(img, (0,0), (300,300), (0,255,0), 3)

# Creates a diogonal line for complete image
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 3)

cv2.imshow("image", img)
cv2.waitKey(0)
