import cv2

cap = VideoCapture(0)

while True:
  ret, frame = cap.read()

  cv2.imshow('output', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows() # Close all windows on the screen
