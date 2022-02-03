# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 00:21:50 2021

@author: ahoth
"""

import cv2
import matplotlib.pyplot as plt
import numpy


def decomposeImage(img: numpy.ndarray, rows:int, cols:int):
    
    image_array = []
    
    height, width = img.shape[0], img.shape[1]
    patch_height = height//rows
    patch_width = width//cols



    x_val = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            part = img[x_val : x_val + patch_height , j*patch_width : j*patch_width + patch_width, ::]
            row.append(part)
            #x_val += width_of_part
            """
            cv2.imshow("part", part)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            """
        x_val += patch_height
        image_array.append(row)
        
        
    f, myPlot = plt.subplots(rows, cols)
    for i in range(rows):
        for j in range(cols):
            print(i, j)
            myPlot[i,j].imshow(image_array[i][j][:,:,::-1])
            print('plotted')
            
    return image_array
    
            

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img6.jpg'

img = cv2.imread(path)

decomposeImage(img, 6, 8)




        
