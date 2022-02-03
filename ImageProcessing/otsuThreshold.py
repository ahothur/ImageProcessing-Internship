# Otsu Threshold


import cv2
import matplotlib.pyplot as plt

def otsuThreshold(img):
    
    # Convert Image to grayscale
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #plt.imshow(grey_img)
    
    ret, thresh = cv2.threshold(grey_img, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
  

    # the window showing output image         
    # with the corresponding thresholding         
    # techniques applied to the input image    
    return thresh
        
"""
path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img1.jpg'

otsuThreshold(path)
"""