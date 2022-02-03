# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 09:22:30 2021

@author: ahoth
"""

# 
# --------- NOT WORKING --------------
#

"""
Using Houghline method for line detection
"""

import cv2
import numpy as np
import sys, types


def lineDetector(img: np.ndarray):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    cv2.imshow('image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # This returns an array of r and theta values
    # Parameters: edge detected image, threshhold for r, theta, threshold votes
    lines = cv2.HoughLines(edges, 1, np.pi/180, 40)
    
    #print(isinstance(lines, types.NoneType))

    
    # If no lines were detected in the image
    if lines is None:
        print("No lines detected")
 
      
    # The below for loop runs till r and theta values 
    # are in the range of the 2d array
    for r,theta in lines[0]:
        
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*r
        y0 = b*r
          
        # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
        x1 = int(x0 + 1000*(-b))
          
        # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
        y1 = int(y0 + 1000*(a))
      
        # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
        x2 = int(x0 - 1000*(-b))
          
        # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
        y2 = int(y0 - 1000*(a))
          
        # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
        # (0,0,255) denotes the colour of the line to be 
        #drawn. In this case, it is red. 
        cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2)
        
        
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return img
    

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img8.jpg'
img = cv2.imread(path)
lineDetector(img)


