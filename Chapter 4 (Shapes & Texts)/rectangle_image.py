'''
This code will create a rectangles (empty and filled) in an image
'''
import cv2
import numpy as np

# Function creates matrix filled with zeros (A black image),
# takes pixels and number of chennels (an optional argument for colored image) as an argument
# zeros --> Black
# ones --> White
img = np.zeros((512,512,3),np.uint8)

# Function creates empty rectangle in an image, takes image, 
# starting and ending point, color of rectangle, and thickness as arguments
cv2.rectangle(img, (0,0), (250,350), (0,255,0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)


# Function creates a filled rectangle
cv2.rectangle(img, (0,0), (250,350), (0,255,0), cv2.FILLED)

cv2.imshow("image", img)
cv2.waitKey(0)
