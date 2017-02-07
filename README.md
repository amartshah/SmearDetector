# SmearDetector
EECS 395 Assignment 1

##Installing
The following dependencies need to be installed via command line to run our script.

conda install opencv  
conda install -c menpo opencv3
echo "backend : TkAgg" > ~/.matplotlib/matplotlibrc


##Run 
python A1.py

##Output
A sequence of images that detect the camera lens smears of the five cameras in the sample_drive folder.

##Resources
We referenced the following resources:

###Canny Edge Detection
http://docs.opencv.org/trunk/da/d22/tutorial_py_canny.html

###Median Blur
http://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html

###Binary Image Thresholding
http://docs.opencv.org/3.2.0/d7/d4d/tutorial_py_thresholding.html
