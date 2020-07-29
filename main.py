import cv2
import numpy as np
vid=cv2.VideoCapture(0)
background=cv2.imread("background.jpg") #we are taking in the background image
while vid.isOpened():
    ret,frame=vid.read() #we are reading the video from the web cam
    if ret==True:   
        hsv_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #converting the bgr value to hsv 
        red=np.uint8([[[0,0,255]]])  
        hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)  #finding the hsv pixels values for red color
        #print(hsv_red)
        
        #the formula for setting lower bound value is hue-10,100,100
        #the formula for setting the higher bound value is hue+10,255,255 
        #we can increase the range for desired results
        
        lower_bound=np.array([0,100,100])   
        higher_bound=np.array([80,255,255])
        mask=cv2.inRange(hsv_image,lower_bound,higher_bound) #assigning the range for red hsv values.
        
#we use morphology to remove the unwanted parts from the image, in this case we are removing the edges from the cloth.
        mask=cv2.morphologyEx(mask, cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
        mask=cv2.morphologyEx(mask, cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
        part1=cv2.bitwise_and(background,background,mask=mask) #here we are masking the backgroung images against the red color pixels
        mask2=cv2.bitwise_not(mask) #for taking in the range of pixels which are "not" red.
        part2=cv2.bitwise_and(frame,frame,mask=mask2)
        masking=part1+part2
        #cv2.imshow("masking",part2)
        cv2.imshow("Invisible",masking)
    if cv2.waitKey(1)==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()








# In[ ]:




