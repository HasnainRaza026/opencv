'''
To crop an image you don't need opencv, you can simply do that by using
matrix functionality
'''
import cv2

img = cv2.imread("image.png")

print(img.shape)

# Resize image using matrix
# [height scale : width scale]
imgCropped = img[0:200, 200:350]

cv2.imshow("cropped image", imgCropped)
cv2.waitKey(0)
