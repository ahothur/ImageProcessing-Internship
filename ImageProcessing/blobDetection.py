# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 11:12:48 2021

@author: ahoth
"""

import cv2
import numpy as np

def blobDetector(img: np.ndarray):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    detector = cv2.SimpleBlobDetector()
    
    keypoints = detector.detect(gray)
    
    blob_img = cv2.drawKeypoints(gray, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('image', blob_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img11.jpg'
img = cv2.imread(path)

blobDetector(img)