import cv2

img = cv2.imread("image.png")

# Function converts image into different color spaces
# takes two arguments an image and a color space function
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray image", imgGray)
cv2.waitKey(0)
