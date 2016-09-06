import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_range = np.array([0,0,0])
    upper_range = np.array([150,150,150])

    mask = cv2.inRange(hsv, lower_range, upper_range)

    result = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((5,5), np.uint8)
    
    #Erosion
    erosion = cv2.erode(mask,kernel,iterations=1)

    #Dilation
    dilation = cv2.dilate(mask,kernel,iterations=1)

    #Opening (Erosion followd by Dilation)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    
    #Closing (Dilation followed by Erosion)
    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    
    cv2.imshow('frame',frame)
    cv2.imshow('result',result)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
    
