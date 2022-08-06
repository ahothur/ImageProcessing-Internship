# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:09:43 2021

@author: ahothur
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Global variable
confidenceThreshold = 0.6


def loadClasses():
    # Funstion to load all categories of objects
    classes = []
    f = open('yolov3.txt', 'r')
    for line in f.readlines():
        classes.append(line.strip())
    return classes

classifications = loadClasses()

#Function to draw the boxes around detected objects in the image
# ---- Still need to Complete -----
def drawBoundingBoxes(image, boxes, confidences, class_ids):
    img = image[:,:,:]      #create image copy
    
    classes = loadClasses()
    
    # For each detection box
    for i in range(len(boxes)):
        box = boxes[i]
        x, y, w, h = int(box[0]), int(box[1]), box[2], box[3]
        #print(x,y,w,h)
        # Draw Box
        cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
        
        #Write Text
        text = classes[class_ids[i]] + " : " + str(round(confidences[i], 3))
        cv2.rectangle(img, (x, y - 15), (x + len(text) * 13, y), (0,0,0), -1)
        cv2.putText(img, text, (x , y), 5, 1, (255,255,255), 1)
        
    return img

# Function to check if cur_box has already been drawn
# to prevent overlapping boxes
# returns True if there is overlap
def checkOverlapBoxes(boxes, cur_box, cur_classid):
    
    for each_box in boxes:
        # if starting point of box is +/- 20 pixels from cur_box
        
        #print("  > In check fn")
        #print("\t", each_box[0], each_box[1], " --- ", cur_box[0], cur_box[1])
        if (abs(each_box[0] - cur_box[0]) <= 25 and abs(each_box[1] - cur_box[1]) <= 25):
            #print("   - ", each_box[0] - cur_box[0], each_box[1] - cur_box[1])
            print(" *** ", classifications[cur_classid])
            return True

    return False


# Function that takes in the image, path of wights file, path of cfg file
# img_out - optional parameter, if we wanted to detect objects in image, but mark them on img_out
# Returns the list of bounding boxes, confidences and classIDs
def usePreTrainedModel(image, weights_path, cfg_path, img_out = None):
    
    model = cv2.dnn.readNet(weights_path, cfg_path)
    
    # Create 4-D blob from image
    # Image, scale factor (normalize to [0,1]), 
    blob = cv2.dnn.blobFromImage(image, 1/255, (320, 320), [0,0,0], swapRB = True, crop = False)
    #print(blob.shape)
    
    # Set blob as input image for the neural network
    model.setInput(blob)
    
    #out_layers = model.getLayerNames()
    out_layers = model.getUnconnectedOutLayersNames()  
    
    # Perform a forward pass on the neural network
    output = model.forward(out_layers)
    
    # Lists for return values
    boxes = []
    confidences = []
    class_ids = []
    

    H = len(image)
    W = len(image[0])
    
        
    for layer in output:
        # print(layer.shape)
        # looping through each object detected in the layer
        for detection in layer:
            #print(detection)
            score = detection[5:] # First few entries record dimensions of bounding box
            class_id = np.argmax(score) # Selects category with highest score
            confidence = score[class_id] # Gets confidence level of that category
            
            #print(confidence)
            
            # Filter objects that were detected with a high probability
            if confidence > confidenceThreshold:
                #print(" >> ", confidence, class_id)
                # detection[0:5] gives center-x, center-y, width and height of bounding box that are SCALED!
                center_x, center_y, width, height = (detection[0:4] *  np.array([W, H, W, H])).astype(int)
                
                # calculate x and y coordiate of bounding box
                x = center_x - width/2
                y = center_y - height/2
                
                # *********************************
                # Check for overlapping boxes
                # *********************************
                if(len(boxes) == 0 or not checkOverlapBoxes(boxes, [x, y, width, height], class_id)):
                    boxes.append([x, y, width, height])
                    confidences.append(confidence)
                    class_ids.append(class_id)
    
    if img_out is not None:
        image = img_out
                
    return drawBoundingBoxes(image, boxes, confidences, class_ids)
                    
            
    

