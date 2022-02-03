# Image Processing funtions
# Archita Hothur
# 12-22-2021

"""
(1) Image Intensity Adjustment 
(2) Image Complement 
(3) Otsu Thresholding 
(4) Image histograms (R G B)Histogram Equalization
"""

import cv2
import matplotlib.pyplot as plt

class ImageModifications:

    def __init__(self, path):
        self.image = cv2.imread(path)
        
    def display(self):
        plt.imshow(self.image[:,:,::-1])
        
    def changeIntensity(self, amt):
        # Convert image to HSV
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        # Add specified amt to image saturation
        s += amt
        hsv = cv2.merge((h,s,v))
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('Intensity', img)
       
        if cv2.waitKey(0):
            cv2.destroyAllWindows()
        
        
    def otsuThreshold(self):
        # Convert Image to grayscale
        grey_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        #plt.imshow(grey_img)
        
        ret, thresh = cv2.threshold(grey_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)     
  
        # the window showing output image         
        # with the corresponding thresholding         
        # techniques applied to the input image    
        cv2.imshow('Otsu Threshold', thresh)
        
        if cv2.waitKey(0):
            cv2.destroyAllWindows() 
            
            
    def showGreyHistogram(self):
        #cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
        grey_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        plt.hist(grey_img.ravel(),256,[0,256])
        plt.show()        
        
    def showRGBHistogram(self):
        img = self.image
        
        color = ('b','g','r')
        for i,col in enumerate(color):
            histr = cv2.calcHist([img],[i],None,[256],[0,256])
            plt.plot(histr,color = col)
            plt.xlim([0,256])
            plt.ylim([0,2000])
            
        plt.show()
        
   
    def dispComplement(self):
        plt.imshow((255 - self.image)[:,:,::-1])
        
        
   
        
        
path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img1.jpg'

myImage = ImageModifications(path)

myImage.display()

#myImage.changeIntensity(15) 

#myImage.dispComplement()
#plt.close()  

#myImage.otsuThreshold()
#plt.close()

myImage.showGreyHistogram()
plt.close()

myImage.showRGBHistogram()
plt.close()
