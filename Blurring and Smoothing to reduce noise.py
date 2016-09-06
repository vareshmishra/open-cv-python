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

    #Averaging Filter
    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(result,-1,kernel)

    #Gaussian Blur
    gblur = cv2.GaussianBlur(result,(15,15),0)

    #Median Blur
    medianblur = cv2.medianBlur(result,15)

    #Bilateral Blur
    bilateral = cv2.bilateralFilter(result,15,75,75)

    cv2.imshow('frame',frame)
    cv2.imshow('result',result)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('gblur',gblur)
    cv2.imshow('medianblur',medianblur)
    cv2.imshow('bilateral',bilateral)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
    
