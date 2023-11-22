import cv2

img = cv2.imread("image.png")

# Function adds blur to an image
# takes 3 arguments an image, a kernal size (ksize, an odd number which defines the value of blur)
# and sigmaX
imgBlur = cv2.GaussianBlur(img, (31,31), 0)

cv2.imshow("gray image", imgBlur)
cv2.waitKey(0)
