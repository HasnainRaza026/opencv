import cv2

# Function reads the webcam, takes one argument (an id of the camera)
cap = cv2.VideoCapture(0)

# Setting perameters (dimension) for the window
cap.set(3,640) #width (id number 3)
cap.set(4,480) #height (id number 4)

# Using webcam is same as of displaying video
while True:
    success, img = cap.read()
    cv2.imshow("Output", img)
    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break
