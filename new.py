import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('cascade.xml')

car=cv2.imread('carnew.jpg')
gray=cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)



cars= car_cascade.detectMultiScale(gray, 3, 30)



for (x,y,w,h) in cars:
    cv2.rectangle(car,(x,y),(x+w,y+h),(255,255,0),2)
    

cv2.imshow('image',car)
cv2.waitKey(0)
cv2.destroyAllWindows()