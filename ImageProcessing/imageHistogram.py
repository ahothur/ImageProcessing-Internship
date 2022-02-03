
"""
Created on Thu Dec 23 12:27:58 2021

@author: ahoth
"""


import cv2
import matplotlib.pyplot as plt
import numpy as np

# Image histogram for grayscale image
def showGreyHistogram(grey_img):
    #grey_img = cv2.imread(path, 0)
    plt.hist(grey_img.ravel(),256,[0,256])
    plt.show()  
    
   
# Image histogram for RGB image
def showRGBHistogram(img):
    
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
        plt.ylim([0,2000])
    plt.show()
    
# Equalize image
def histogramEqulization(grey_img):
    equ = cv2.equalizeHist(grey_img)
    res = np.hstack((grey_img,equ))
    cv2.imshow("result", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return equ
    
    
    
path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img4.jpg'

grey_img = cv2.imread(path, 0)

showGreyHistogram(grey_img)

equ = histogramEqulization(grey_img)

showGreyHistogram(equ)

##showGreyHistogram(path)
#plt.close()

"""
plt.plot(showGreyHistogram(myImage))
plt.show()
"""