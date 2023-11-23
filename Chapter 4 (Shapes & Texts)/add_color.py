'''
This code adds a colored box in an image
To add any colored shape or text in an image we manipulate matrix
using numpy
'''
import cv2
import numpy as np

# Function creates matrix filled with zeros (A black image),
# takes pixels and number of chennels (an optional argument for colored image) as an argument
# zeros --> Black
# ones --> White
img = np.zeros((512,512,3),np.uint8)

# To color the complete image blue
# [:] --> complete height and width
# img[:] = 255,0,0

# To color the portion of image blue
img[200:300, 100:300] = 255,0,0

cv2.imshow("image", img)
cv2.waitKey(0)
