# Reading Image
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
![coca-cola](https://github.com/HasnainRaza026/opencv/assets/138324430/345354c0-79a4-4985-8528-3b3204ec9cf0)

## EXAMPLE
```py
# Read image as gray scale.
img = cv2.imread("checkerboard.jpg", 0)

# print image
print(img)

# Display image.
cv2.imshow(img)
```

[[  0   0  15  20   1 134 233 253 253 253 255 229 130   1  29   2   0   0]
 [  0   1   5  18   0 137 232 255 254 247 255 228 129   0  24   2   0   0]
 [  7   5   2  28   2 139 230 254 255 249 255 226 128   0  27   3   2   2]
 [ 25  27  28  38   0 129 236 255 253 249 251 227 129   0  36  27  27  27]
 [  2   0   0   4   2 130 239 254 254 254 255 230 126   0   4   2   0   0]
 [132 129 131 124 121 163 211 226 227 225 226 203 164 125 125 129 131 131]
 [234 227 230 229 232 205 151 115 125 124 117 156 205 232 229 225 228 228]
 [254 255 255 251 255 222 102   1   0   0   0 120 225 255 254 255 255 255]
 [254 255 254 255 253 225 104   0  50  46   0 120 233 254 247 253 251 253]
 [252 250 250 253 254 223 105   2  45  50   0 127 223 255 251 255 251 253]
 [254 255 255 252 255 226 104   0   1   1   0 120 229 255 255 254 255 255]
 [233 235 231 233 234 207 142 106 108 102 108 146 207 235 237 232 231 231]
 [132 132 131 132 130 175 207 223 224 224 224 210 165 134 130 136 134 134]
 [  1   1   3   0   0 129 238 255 254 252 255 233 126   0   0   0   0   0]
 [ 20  19  30  40   5 130 236 253 252 249 255 224 129   0  39  23  21  21]
 [ 12   6   7  27   0 131 234 255 254 250 254 230 123   1  28   5  10  10]
 [  0   0   9  22   1 133 233 255 253 253 254 230 129   1  26   2   0   0]
 [  0   0   9  22   1 132 233 255 253 253 254 230 129   1  26   2   0   0]]

 ![checkbox_blur](https://github.com/HasnainRaza026/opencv/assets/138324430/e70f2856-03f2-445d-8438-db4e0126480e)



# Write Image
OpenCV allows writing image (saving to the sepcified path) using **imwrite()** function

## Function Syntax
```py
cv2.imwrite(filename, img, parameter)
```
### Parameters
The function has **2 required input argument** and one optional **flag**:
1. `filename`: This can be an **absolute** or **relative path**. This is a mandatory argument

2. `img`: Image or Images to be saved

3. `parameter`: An optional flag used to specify the format of the img to be save

To see the falgs visit below documentation

## OpenCV Documentation
1. `imwrite`: [Documentation link](https://docs.opencv.org/4.5.1/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce)
2. `ImwriteFlags`: [Documentation link](https://docs.opencv.org/4.5.1/d8/d6a/group__imgcodecs__flags.html#ga292d81be8d76901bff7988d18d2b42ac)

## EXAMPLE
```py
# Read image in actual format (colored)
img = cv2.imread("shapes.png")

# Convert to gray-scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save image to the same directory
cv2.imwrite("img_gray.png", img_gray)
```

This image will be saved in the directory

![img_gray](https://github.com/HasnainRaza026/opencv/assets/138324430/c8b77ee4-c081-4e2b-84d8-9b0aa6f44185)


# Splitting and Merging Color Channels