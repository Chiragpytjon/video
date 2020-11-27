import cv2, time

#1 create an object. Zero for external camera
video=cv2.VideoCapture(0)


#construct a while loop
a=0
while True:
    a = a+1

    #3 create a frame object
    check, frame = video.read()


    #6 converting to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY )


    print(check)
    print(frame)  #repesenting image


    #4 show the frame
    cv2.imshow('thupun', gray)



    #5 set that any key will break the capturing(milliseconds)
    #cv2.waitKey(0)

    #for playing
    key=cv2.waitKey(1)

    if key == ord('q'):
        break


print(a)
#2 shutdown the camera
video.release()
cv2.destroyAllWindows
