# Imcreasing image intensity

import cv2
import matplotlib.pyplot as plt
from PIL import Image

# Funtion to change image with changed intensity by amount specified by parameter
# Returns the image of changed intensity

def changeImageIntensity(path, amt):
    image = cv2.imread(path)
    # Convert image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    # Add specified amt to image saturation
    s += amt
    hsv = cv2.merge((h,s,v))
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return img[:,:,::-1]
    


"""
path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img1.jpg'

changeImageIntensity(path, 5)
"""

