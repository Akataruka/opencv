import  cv2 as cv

#Changing the size of the image and videos and live video from webcam
def resize(frame, scale=0.25):
    #Works for images,video and Live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

#Changing Resolution of the live webcam
def changeRes(width, height):
    #Works on Live videos
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('videos/video1.mp4')

while True:
    isTrue, frame = capture.read()
    if isTrue:
        frame_resized = (
            resize(frame))

        cv.imshow('video', frame)
        cv.imshow('video_resized', frame_resized)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)