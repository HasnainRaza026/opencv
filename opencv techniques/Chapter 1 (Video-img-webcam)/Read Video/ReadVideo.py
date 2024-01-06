import cv2

# Function reads the videos and store it in a varible
vid = cv2.VideoCapture("video.mp4")

# As the video is a combination of different images (Frames), hence
# the video is displayed by displaying its different frames, with time delay
# and for that we use while loop to display each frame of the video
while True:
    # Fuction read each frame of the video and store it in img variable,
    # 'success' variable returns boolean value true if this operation is successful
    success, img = vid.read()

    # Display each frame of the video
    cv2.imshow("Output", img)

    # if 'q' is pressed, the window will close
    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break
