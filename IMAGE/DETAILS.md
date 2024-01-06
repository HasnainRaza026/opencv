# Reading images using OpenCV
OpenCV allows reading different types of images (JPG, PNG, etc). You can load grayscale images, color images or you can also load images with Alpha channel. It uses the **cv2.imread()** function which has the following syntax:
## Function Syntax
```py
retval = cv2.imread(filename, [flags])
```
`retval`: Is the image if it is successfully loaded. Otherwise it is `None`. This may happen if the filename is wrong or the file is corrupt.

### Parameters
The function has **1 required input argument** and one optional flag:

1. `filename`: This can be an **absolute** or **relative** path. This is a **mandatory argument**.

2. `Flags`: These flags are used to read an image in a particular format (for example, grayscale/color/with alpha channel). This is an **optional argument** with a default value

Before we proceed with some examples, let's also have a look at some of the `flags` available.

**Flags**

1. `cv2.IMREAD_GRAYSCALE` or `0`: Loads image in grayscale mode
2. `cv2.IMREAD_COLOR` or `1`: Loads a color image. Any transparency of image will be neglected. It is the default flag.
3. `cv2.IMREAD_UNCHANGED` or `-1`: Loads image as such including alpha channel.

## OpenCV Documentation
1. `Imread`: [Documentation link](https://docs.opencv.org/4.5.1/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56)
2. `ImreadModes`: [Documentation link](https://docs.opencv.org/4.5.1/d8/d6a/group__imgcodecs__flags.html#ga61d9b0126a3e57d9277ac48327799c80)

## EXAMPLE
Consider th following image:

![checkbox](https://github.com/HasnainRaza026/opencv/assets/138324430/156ef1d3-dc35-466b-908c-c919e5bc3854)

```py
# Read image as gray scale.
cb_img = cv2.imread("checkerboard_18x18.png", 0)

# Print the image data (pixel values), element of a 2D numpy array.
# Each pixel value is 8-bits [0,255]
print(cb_img)
```

[[  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [255 255 255 255 255 255   0   0   0   0   0   0 255 255 255 255 255 255]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]
 [  0   0   0   0   0   0 255 255 255 255 255 255   0   0   0   0   0   0]]


# Display Image attributes

```py
# print the size  of image
print("Image size (H, W) is:", cb_img.shape)

# print data-type of image
print("Data type of image is:", cb_img.dtype)
```
Image size (H, W) is: (18, 18)

Data type of image is: uint8


# Display Image
OpenCV allows to display image in a specified window using **imshow()** function

## Function Syntax
```py
cv2.imshow(WinName, img)
```

### Parameters
The function has **2 required input arguments**

1. `WinName`: Name of the window

2. `img`: Image to be shown

**Note:**
This function should be followed by cv::waitKey function which displays the image for specified milliseconds. Otherwise, it won't display the image. For example, waitKey(0) will display the window infinitely until any keypress (it is suitable for image display). waitKey(25) will display a frame for 25 ms, after which display will be automatically closed. (If you put it in a loop to read videos, it will display the video frame-by-frame)

## OpenCV Documentation
1. `imshow`: [Documentation link](https://docs.opencv.org/4.5.1/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563)
2. `waitKey`: [Documentation link](https://docs.opencv.org/4.5.1/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7)


## EXAMPLE
```py
# Read the image in original format
img = cv2.imread("coca-cola.png")

# Display the image
cv2.imshow("output", img)
# Wait untill any key is pressed
cv2.waitKey(0)
```
