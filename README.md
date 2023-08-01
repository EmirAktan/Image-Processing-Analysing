# Image-Processing-Analysing
Image Processing/Analayzing tool for calculating surface area of objects (in this case microglia).
There is two algorithms:
* One of them directly analyzes the picture from microscopy and creates an outline for the ROI (region of interest), gives a number to the specific ROI's and calculates its area (surface area).
* For the other one use the Fiji's machin learning algorithm for segmentation. After training the model it will give you a good segmentation of the microscopy image. After that use that image in the algorithm to get the best result.
    * Both of them uses already thresholded images. These algorithms creates a more reliable outlines than Fiji for the '*irregular*' shapes.
