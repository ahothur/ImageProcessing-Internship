# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 10:18:32 2021

@author: ahoth
"""

# Circle detection


# ---- problem -> detecting too many false circles!!

import cv2
import numpy as np

def circleDetector(img: np.ndarray):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.blur(gray, (6, 6))
    edges = cv2.Canny(gray_blurred, 50, 150, apertureSize = 3)
    
    cv2.imshow('image', gray_blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow('image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    circles = cv2.HoughCircles(edges,    #image
                               cv2.HOUGH_GRADIENT,  #method to detect circles
                               1,   #dp - large dp => small accumulator
                               100,  #min dist
                               param1 = 1,
                               param2 = 5,
                               minRadius = 10,
                               maxRadius = 75)
    if circles is not None:
        circles = np.uint16(np.around(circles))
  
    for pt in circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 0, 255), 2)
            
    		
     
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
           
           

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img9.jpg'
img = cv2.imread(path)

circleDetector(img)