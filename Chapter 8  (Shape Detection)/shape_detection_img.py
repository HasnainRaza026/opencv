import cv2
import numpy as np

# Function to stack multiple images/videos
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


def getContours(img):
    # function find coonotours (shapes) in an image,
    # cv2.RETR_EXTERNAL gets the extreme contours in an image (used in finding outer corners)
    # cv2.CHAIN_APPROX_NONE gets all the contours found (uncompressed)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  
    for cnt in contours:
        # Function finds the area os the contour (shape)
        area = cv2.contourArea(cnt)
        print(area)

        if area>500:
            # Function draws the controus on the image
            # -1 means to dra all the contours
            cv2.drawContours(img_copy, cnt, -1, [255,0,0], 3)

            # Function finds the arc length of the contours (helps to finds cornors)
            # True indicates that the shape is closed
            arc_len = cv2.arcLength(cnt, True)
            print(arc_len)

            # Function finds the cornor points in a contour
            # 0.02*arc_len is the resolution
            # True indicates that the shape is closed
            approx = cv2.approxPolyDP(cnt, 0.02*arc_len, True)
            print(len(approx))
            obj_cornor = len(approx)

            GetBoundingBox(approx, obj_cornor)



def GetBoundingBox(approx, obj_cornor): 
    x, y, w, h = cv2.boundingRect(approx)
    cv2.rectangle(img_copy, (x, y), (x+w, y+h), [0,255,0], 3)

    if obj_cornor==3:
        Objtype = "Tri"
    elif obj_cornor==4:
        ratio = w/float(h)
        if ratio>=0.95 or ratio<=1.05:
            Objtype="square"
        else:
            Objtype="rectangle"
    else:
        Objtype="circle"

    cv2.putText(img_copy,  
                Objtype,  
                (x+(w//2)-10,y+(h//2)-10),  
                cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                (0, 0, 0),  
                2) 


img = cv2.imread("shapes.png")

# makes the copy of an original image
img_copy = img.copy()

# a blank black image
img_black = np.zeros_like(img)

# cnverting image to gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# adding some blur to dray image, (7,7) is the ernal value and 1 is the blur value
img_blur = cv2.GaussianBlur(img_gray, (7,7), 1)

# Finding edges using Canny edge detector function
img_cany = cv2.Canny(img_blur, 50, 50)

getContours(img_cany)

img_stk = stackImages(0.6, ([img, img_gray, img_black],[img_blur, img_cany, img_copy]))

cv2.imshow("output", img_stk)
cv2.waitKey(0)
