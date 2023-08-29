# Image-Processing-Analysing
Image Processing/Analayzing tool for calculating surface area of objects (in this case microglia).
There is two algorithms:
* One of them directly analyzes the picture from microscopy and creates an outline for the ROI (region of interest), gives a number to the specific ROI's and calculates its area (surface area).
* For the other one use the Fiji's machin learning algorithm for segmentation. After training the model it will give you a good segmentation of the microscopy image. After that use that image in the algorithm to get the best result.
    * Both of them uses already thresholded images. These algorithms creates a more reliable outlines than Fiji for the '*irregular*' shapes.
    * While using the 'import_blackarea_calculaator.py' the ROI should be black and background should be white.
    * The opposite process should be done for 'white areas nearlyfinal.py' the ROI should be white and background should be black. (normal mask)
 
Protocol:

You need to download any code editor that can run python and its versions. Visual studio code is preferred. You can download Visual Studio Code from https://code.visualstudio.com/download. 

After downloading and opening the VS Code, go to extensions and type Python and download it. 

Go to File --> New File --> Pyhton File

Then you can copy the codes to your new python file or download it from github. 

1) If you want to use segmentation from Fiji, you can go to Fiji's search engine and search Trainable Segmentation. After that you need to select the tool that is in the attached pictures.
2) Then you need to draw lines in region of interest (ROI) and the background. Each time after you draw a line, click add to class 1 or class 2. For example, in this case class 1 is microglias and class 2 is background. 
3) Train the classifier and create results.
4) Go to Fiji console and File --> Save As --> PNG.
5) After saving the picture as png go find the picture Right Click --> Copy as path
6) After doing that copy the path on the image path part in the code.
7) Also since this is a PNG there is no metadata in the picture itself. Go to Fiji's console --> Image --> Show Info --> Go to the end of the log --> Voxel Size --> Take the first two parameters and copy it to the pixel area in the code.
8) Edit the output path of the image as in the attached files. 
9) Run the code by clicking Run Python File at the upper right of the page.
10) Image output is shown with a new panel open. Also it downloads that image to the path you chose with the excel file.  

1)![resim](https://github.com/EmirAktan/Image-Processing-Analysing/assets/115092603/dac8d7da-f003-4056-ad3a-0f58bcc0a5e0)
2)![resim](https://github.com/EmirAktan/Image-Processing-Analysing/assets/115092603/4aecbb77-a3e3-49d2-b4e6-717f0ea4b106)
6 & 7) ![resim](https://github.com/EmirAktan/Image-Processing-Analysing/assets/115092603/9dfec358-9840-4645-a1f4-c4bf58d9a9df)
7)![resim](https://github.com/EmirAktan/Image-Processing-Analysing/assets/115092603/1499f160-2d15-4cea-a0f1-9ee6c45b492c)
8)![resim](https://github.com/EmirAktan/Image-Processing-Analysing/assets/115092603/ff837bed-009d-4276-9f86-495edc52bc24)



