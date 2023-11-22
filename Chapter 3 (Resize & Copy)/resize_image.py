import cv2

img = cv2.imread("image.png")

# Finds the size of the image
# Output --> (height, width, channel number)
print(img.shape)

# Function resizes the image, takes two arguements, an image
# and a tuple containing width and height (you want change to)
imgResize = cv2.resize(img, (200,200))

cv2.imshow("edge image", imgResize)
cv2.waitKey(0)
