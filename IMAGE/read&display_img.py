import cv2

# function to read the image and store in a variable
img = cv2.imread("image.png")

# This function displays the image on screen, it takes 2 arguments
# the name of the window (any name) and the image
cv2.imshow("Output", img)

# function to keep the the image window open for the defined time
# 0 means infinite time, any integer (1, 1000 etc) means that many miliseconds
cv2.waitKey(0)
