import numpy as np
import cv2
import os, os.path
from matplotlib import pyplot as plt
import scipy.ndimage as ndi
#from skimage import filters


#main folder
path = 'sample_drive'

#dictionary, key is camera, value is list of corresponding images
camera_images = {
    'cam_0':[],
    'cam_1':[],
    'cam_2':[],
    'cam_3':[],
    'cam_5':[]
}

#iterate through each camera folder
for folder in os.listdir(path):
    #skip
    if folder == '.DS_Store':
        pass
        
    #load images, append to dict's list - only 10 per folder for now
    else:
        counter = 0
        for pic in os.listdir(path+ '/' + folder):
            if counter == 30:
                break
            #full path
            pic_path = path+ '/' + folder + '/' + pic
            #Load color image in grayscale
            img = cv2.imread(pic_path,0)
            camera_images[folder].append(img)
            counter += 1
    
masks = []
#basic logic for canny edge detection
for camera in camera_images:
    canny_images = []
    for i in xrange(len(camera)):
        img = camera_images[camera][i]
        edges = cv2.Canny(img,50,135)
        #print edges
        canny_images.append(edges)
    
    average = np.average(canny_images, axis=0)
    masks.append(average)
        
        
for mask in masks:
    mask = mask.astype(np.uint8)

    mask = ndi.gaussian_filter(mask, (10,10))
    mask = cv2.medianBlur(mask, 111)

    ret4,th4 = cv2.threshold(mask,1,1,cv2.THRESH_BINARY)

    plt.imshow(th4,cmap = 'gray')
    plt.title('Camera Mask'), plt.xticks([]), plt.yticks([])

    plt.show()            
