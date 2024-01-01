import cv2
import numpy as np


# Creating Trackbars
# -----------x----------------x--------------------x-----------------
def empty(a):
    pass

cv2.namedWindow("Parameter")
cv2.resizeWindow("Parameter", 640, 240)
cv2.createTrackbar("Threshold", "Parameter", 200, 255, empty)
cv2.createTrackbar("Threshold", "Parameter", 200, 255, empty)
# cv2.createTrackbar("Area", "Parameter", 0.5, 1, empty)
# cv2.createTrackbar("Area", "Parameter", 1, 1.5, empty)
# -----------x-----------------x--------------------x-----------------



# Function to stack multiple images/videos
# -----------x----------------x--------------------x-----------------
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
# -----------x----------------x--------------------x-----------------



# Functin to get contours (shapes) in a frame
# -----------x----------------x--------------------x-----------------
def getContours(frame_dill,frame_copy):
    # function find coonotours (shapes) in an image,
    # cv2.RETR_EXTERNAL gets the extreme contours in an image (used in finding outer corners)
    # cv2.CHAIN_APPROX_NONE gets all the contours found (uncompressed)
    contours, hierarchy = cv2.findContours(frame_dill, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  
    for cnt in contours:
        # Function finds the area os the contour (shape)
        area = cv2.contourArea(cnt)
        print(area)

        if area>500:
            # Function draws the controus on the image
            # -1 means to dra all the contours
            cv2.drawContours(frame_copy, cnt, -1, [255, 0, 255], 7)

            # Function finds the arc length of the contours (helps to finds cornors)
            # True indicates that the shape is closed
            arc_len = cv2.arcLength(cnt, True)
            #print(arc_len)

            # Function finds the cornor points in a contour
            # 0.02*arc_len is the resolution
            # True indicates that the shape is closed
            approx = cv2.approxPolyDP(cnt, 0.02*arc_len, True)
            #print(len(approx))
            obj_cornor = len(approx)

            GetBoundingBox(approx, obj_cornor, area)
# -----------x----------------x--------------------x-----------------
            


# Function to get boundingbox on the detected sahpes
# -----------x----------------x--------------------x-----------------
def GetBoundingBox(approx, obj_cornor, area): 
    x, y, w, h = cv2.boundingRect(approx)
    cv2.rectangle(frame_copy, (x, y), (x+w, y+h), [255,0,0], 5)

    if obj_cornor==3:
        Objtype = "Tri"
    elif obj_cornor==4:
        # threshold3 = cv2.getTrackbarPos("Area", "Parameter")
        # threshold4 = cv2.getTrackbarPos("Area", "Parameter")
        ratio = w/float(h)
        if ratio>=0.95 or ratio<=1.05:
            Objtype="square"
        else:
            Objtype="rectangle"
    elif obj_cornor==5:
        Objtype="pentagone"
    elif obj_cornor==6:
        Objtype="hexagone"
    else:
        Objtype="circle"

    cv2.putText(frame_copy,  
                Objtype,  
                (x+w+20, y+20),  
                cv2.FONT_HERSHEY_COMPLEX, 0.7,
                (255, 0, 0),  
                2) 
# -----------x----------------x--------------------x-----------------



cap = cv2.VideoCapture(1)

while True:
    succcess, frame = cap.read()
    frame_copy = frame.copy()

    frame_blur = cv2.GaussianBlur(frame, (7,7), 1)
    frame_gray = cv2.cvtColor(frame_blur, cv2.COLOR_BGR2GRAY)


    threshold1 = cv2.getTrackbarPos("Threshold", "Parameter")
    threshold2 = cv2.getTrackbarPos("Threshold", "Parameter")
    fram_canny = cv2.Canny(frame_gray, threshold1, threshold2)

    # To reduce the noice in canny frame
    kernal = np.ones([5,5])
    frame_dill = cv2.dilate(fram_canny, kernal, iterations=1)

    getContours(frame_dill,frame_copy)

    frame_stk = stackImages(0.5, ([frame, frame_gray, fram_canny], [frame_dill, frame_copy, frame_dill]))

    cv2.imshow("output", frame_stk)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
