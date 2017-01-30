import numpy as np
import cv2
import os, os.path
from matplotlib import pyplot as plt


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
            if counter == 10:
                break
            #full path
            pic_path = path+ '/' + folder + '/' + pic
            #Load color image in grayscale
            img = cv2.imread(pic_path,0)
            camera_images[folder].append(img)
            counter += 1
    
#basic logic for canny edge detection
for camera in camera_images:
    for i in xrange(len(camera)):
        img = camera_images[camera][i]
        edges = cv2.Canny(img,100,200)
        print edges
        plt.subplot(121),plt.imshow(img,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        #plt.show()            
