"""
Created on Fri Dec 24 09:08:12 2021

@author: ahoth
"""

# Image Add

import cv2
import numpy

# Function to add a constant value to each channel

def imageAdd1(img: numpy.ndarray, amt: int):
    print("One image")
    
    b, g, r = cv2.split(img)
    b += amt
    g += amt
    r += amt
    
    joined_img = cv2.merge((b, g, r))
    
    cv2.imshow("part", cv2.vconcat([img, joined_img]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return joined_img


#Function to blend two images together
def imageAdd2(img1: numpy.ndarray, img2: numpy.ndarray):
    print("2 images")
    img = cv2.add(img1, img2) 
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return img
    

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img5.jpg'
img = cv2.imread(path)
imageAdd1(img, 5)


p1 = path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img7.jpg'
p2 = path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img7b.jpg'
imageAdd2(cv2.imread(p1), cv2.imread(p2))

