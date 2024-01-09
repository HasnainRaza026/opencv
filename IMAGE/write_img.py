import cv2

# Read image in actual format (colored)
img = cv2.imread("shapes.png")

# Convert to gray-scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save image to the same directory
cv2.imwrite("img_gray.png", img_gray)

print("success")