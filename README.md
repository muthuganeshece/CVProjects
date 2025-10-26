8# CVProjects
Hi 👋🏾 Welcome to my Computer Vision Projects Repository! This repository contains all my work related to Computer Vision and Deep Learning

# Contents
- **Computer Vision based Automation System for Sodium Disposal Plant**
- **Motion Debluring of Scintillator based Optical images from an X-ray source**
- **Neural network based Blind Denoising of X-ray images**
- **Colorimetric Analysis for Chemical Compound Estimation**

# Real time Computer Vision based Automation System for Sodium Disposal Plant
- **Tools and Libraries:**
  - Python, Numpy, Open-CV, Ultralytics, YOLOv8, Roboflow, PyTorch
- **Architectures:**
  - YOLOv8, LSTM
- **Project Description:**
  - Efficient disposal of sodium
## Annotation 
- Convert experiment video in asf format to Open- CV compatible mp4 format 
- Extract video clips from the full video of the experiments using ImageExtraction.ipynb
- To generalize the dataset all possible combinations are captured ie. fire during low, very low visibilities, out of focus, sputtering fire etc.,
- Apply annotation for image segmentation task
- Apply image augmentation
## Sodium Fire Segmentation
- Semantic Segmentation of fire from the raw image
- Annotate dataset using Roboflow
- Yolo v8 pretrained segmentation model is used to train custom dataset

## Detection of Hydrogen Buildup
- Characterization study on sequence of images to detect hydrogen combustion
- Feature extraction from each image
- Sequence modeling for hydrogen burst detection


## Visibility Estimation
- Edge detection based Visibility Estimation algorithm is used
- Thresholding to be added

## Deployment 
- Edge deployment on NVIDIA Orin Nano board
- Linux OS
- GPU acceleration 

# Motion Debluring of Scintillator based Optical images from an X-ray source
- **Tools and Libraries:**
  - Python, Numpy, Open-CV, TensorFlow, Scipy
- **Architectures:**
  - 
- **Project Description:**
  - Optical images captured from the scintillator which emit photons when exposed to X-rays
  - Rapid motion of the object being imaged causes the captured images to suffer from blur
  - The blur effect reduces the clarity and accuracy of the images
  - This makes it difficult to extract precise information about the object's location and features
  - Advanced image deblurring techniques are needed to restore image sharpness and accurate localization of the object
  - The object of interest is spherical in nature with the diameter of 10mm

## Image Preprocessing
- Adjusted the brightness of 16-bit images for better visibility of the object
- Applied flat field correction to separate the foreground from the background
- Used a Gaussian filter for smoothing
- Binarized the image by applying thresholding techniques
  
## Estimation of Point Spread Function
- using blind deconvolution method
