# 12-20-2021
# Funtion to display an image given its path

#Import Libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt


#Display an image



#Funstion to open an image given its path
def dispImage(path):
    img = cv2.imread(path)
    img = img[:, :, ::-1]
    plt.imshow(img)
    
    
p = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/sample-img.jpg'
dispImage(p)
    

