'''
Basic functions of openCv that are used during the projects
'''

import cv2 as cv

img = cv.imread('images/pic1.jfif')
cv.imshow('Original', img)

# Converting to grey scale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur an Image
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dilating the Image
dilated = cv.dilate(blur, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Erode the Image
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize an Image
resize = cv.resize(img, (500,500))
cv.imshow('Resized', resize)

# Cropping an Image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)