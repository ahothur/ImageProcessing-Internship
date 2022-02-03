# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 10:12:50 2021

@author: ahoth
"""

# warpImages

import cv2
import numpy as np

# Affine Transformation
# Lines that are parallel in original image remailn parallel in warped image
# pts1: points in original image
# pts2: location of pts1 in warped image
def affineTransform(img: np.ndarray, pts1: np.ndarray, pts2: np.ndarray):
    rows, cols, ch = img.shape
      
    # M is the transformation matrix
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows))
    
    cv2.imshow('image', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return dst

# Perspective Transform
# ---- right now works only with hard-coded values ----
# pts1: points in original image
# pts2: location of pts1 in warped image
def perspectiveTransform(img: np.ndarray, pts1: np.ndarray, pts2: np.ndarray):
    
    M = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, M, (400, 600))
    
    cv2.imshow('image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
    
path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img6.jpg'
img = cv2.imread(path)

pt1 = np.float32([[50, 50], 
                   [200, 50],
                   [50, 200]])
  
pt2 = np.float32([[50, 100],
                   [160, 70], 
                   [100, 250]])

affineTransform(img, pt1, pt2)



path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img12.jpg'
img = cv2.imread(path)

cv2.circle(img, (95, 185), 1, (0, 0, 0), 2)
cv2.circle(img, (275, 85), 1, (0, 0, 0), 2)
cv2.circle(img, (380, 360), 1, (0, 0, 0), 2)
cv2.circle(img, (550, 220), 1, (0, 0, 0), 2)

pts1 = np.float32([[95, 185], [275, 85], [380, 360], [550,220]])
pts2 = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

perspectiveTransform(img, pts1, pts2)


