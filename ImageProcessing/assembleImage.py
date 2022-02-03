"""
Created on Fri Dec 24 01:02:27 2021

@author: ahoth
"""

import cv2
import decomposeImage

def assembleImage(list_of_parts: list):   
    
    # List to contain images joined horizontally
    row_img = []
    print(len(list_of_parts))
    for i in range(len(list_of_parts)):
        row_img.append(cv2.hconcat(images_to_join[i]))
        
    joined_image = cv2.vconcat(row_img)
    
    cv2.imshow("part", joined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img6.jpg'

img = cv2.imread(path)

r = 4
c =  3
images_to_join = decomposeImage.decomposeImage(img, r, c)

assembleImage(images_to_join)



    
    

        




