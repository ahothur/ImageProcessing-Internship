# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 20:45:30 2021

@author: ahoth
"""

# Image Pyramids
# Changing resolution of images
# Pyramids can be used for image blending

import cv2
import numpy as np

def imagePyramid(img: np.ndarray):
    image_pyramid = [img]
    
    # Creating copy of image
    lower_res = img[:,:,:]
    
    for i in range(3):
        lower_res = cv2.pyrDown(lower_res)
        image_pyramid.insert(0, lower_res)
        
    # Creating copy of image
    higher_res = img[:,:,:]
    
    for i in range(3):
        higher_res = cv2.pyrUp(higher_res)
        image_pyramid.append(higher_res)
        
    """    
    for image in image_pyramid:
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    """
    return image_pyramid
    
path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img6.jpg'
img = cv2.imread(path)

imagePyramid(img)
