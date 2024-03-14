'''
Drawing shapes on images and  videos
'''

import cv2 as cv
import  numpy as np

#Creating blank image to work with
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[:] = 0,255,0
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) 

# can be useed thickness as -1 for completely filling the image
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (250,250), 40, (0,0,250), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (250,250), (255,0,0), thickness=3)
cv.imshow('Line', blank)

# 5. Write text on a image
cv.putText(blank, 'Hello',(255,255), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)