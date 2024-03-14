import  cv2 as cv

'''
#Reading images in opencv
#reading the picture from a specific directory using imread() function
img = cv.imread('./images/pic1.jfif')

#to show the readed picture use the imshow() function
cv.imshow('Cat', img)

#waitkey(0) let the window to be open for a specific amount of time for the key to pressed
cv.waitKey(0)
'''

#Reading videos in Opencv

#Reading video using VideoCapture() function 0,1,2 can be used to access different devices of the pc
#or path link can be given

capture = cv.VideoCapture('videos/video1.mp4')

while True:
    isTrue, frame = capture.read()
    if isTrue:
        cv.imshow('video', frame)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
