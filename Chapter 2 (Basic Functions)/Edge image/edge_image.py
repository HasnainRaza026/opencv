import cv2

img = cv2.imread("image.png")

# Function finds the edges in an image, takes two arguments
# an image and a threshold values
imgEdge = cv2.Canny(img, 100, 100)

cv2.imshow("edge image", imgEdge)
cv2.waitKey(0)
