
#this is a simple code to get the backgroud image.
import cv2
vid=cv2.VideoCapture(0)
while vid.isOpened():
    ret,frame=vid.read()
    if ret==True:
        cv2.imshow("screen",frame)
    if cv2.waitKey(1)==ord('q'):
        cv2.imwrite("background.jpg",frame)
        break
vid.release()
cv2.destroyAllWindows()

