'''
This code will create a circle in an image
'''
import cv2
import numpy as np

# Function creates matrix filled with zeros (A black image),
# takes pixels and number of chennels (an optional argument for colored image) as an argument
# zeros --> Black
# ones --> White
img = np.zeros((512,512,3),np.uint8)

# Function creates a circle in an image, takes image, 
# center point, radius, color, and thickness as arguments
cv2.circle(img, (400,50), 30, (255,255,0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
