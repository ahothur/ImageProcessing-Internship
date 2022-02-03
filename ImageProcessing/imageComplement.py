# Convert image to its complement
"""
Created on Thu Dec 23 12:13:54 2021

@author: ahoth
"""

import matplotlib.pyplot as plt

def dispComplement(image):
     return (255 - image)[:,:,::-1]