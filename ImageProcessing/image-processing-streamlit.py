


import streamlit as st
import cv2
import imageIntensity
import otsuThreshold
import imageComplement
import imageHistogram

st.title("Image Processing Techniques")

#
#****** CHANGING IMAGE INTENSITY *********
#

st.header("1. Changing Image Intensity")

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img1.jpg'


st.subheader("Original Image")
myImage = cv2.imread(path)
st.image(myImage[:,:,::-1])

amt = st.slider("Change image intensity", 0, 50)

st.subheader("Modified Image")
myImage = imageIntensity.changeImageIntensity(myImage, amt)
st.image(myImage)


#
#    ******* IMAGE COMPLEMENT *********
#

st.header("2. Inverting Image")

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img3.jpg'

st.subheader("Original Image")
myImage = cv2.imread(path)
st.image(myImage[:,:,::-1])

st.subheader("Modified Image")
myImage = imageComplement.dispComplement(myImage)
st.image(myImage)


#
#    ******* OTSU THESHOLD *********
#

st.header("3. Otsu Threshold")

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img2.jpg'

st.subheader("Original Image")
myImage = cv2.imread(path)
st.image(myImage[:,:,::-1])

st.subheader("Modified Image")
myImage = otsuThreshold.otsuThreshold(myImage)
st.image(myImage)

#
#    ******* IMAGE HISTOGRAM *********
#

st.header("3. Image Histograms")

path = 'C:/Users/ahoth/OneDrive/Desktop/Internship/Dec2021-Avail/Code/availintern/Images/img4.jpg'

st.subheader("Greyscale Image")
myImage = cv2.imread(path, 0)
st.image(myImage)

"""
st.subheader("Histogram")
hist = imageHistogram.showGreyHistogram(myImage)
st.pyplot(hist)
"""
