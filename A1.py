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
        edges = cv2.Canny(img,100,200)
        #print edges
        canny_images.append(edges)
    
    average = np.average(canny_images, axis=0)
    masks.append(average)
        
        
for mask in masks:
    mask = mask.astype(np.uint8)

    mask = ndi.gaussian_filter(mask, (10,10))
    mask = cv2.medianBlur(mask, 111)

    # blur = cv2.GaussianBlur(mask,(5,5),0)
    ret4,th4 = cv2.threshold(mask,1,1,cv2.THRESH_BINARY)

    #ret3,th3 = cv2.threshold(mask,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #image_final, contours, hierarchy = cv2.findContours(th4,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #mask = cv2.drawContours(image_final, contours, -1, (0,255,0), 3)
    
    #####UNCOMMENT BELOW FOR AN ATTEMPT AT FOREGROUND IDENTIFICATION
    # ret, thresh = cv2.threshold(mask,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # # noise removal
    # kernel = np.ones((3,3),np.uint8)
    # opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    #
    # # sure background area
    # sure_bg = cv2.dilate(opening,kernel,iterations=3)
    #
    # # Finding sure foreground area
    # dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    # ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    #
    # # Finding unknown region
    # sure_fg = np.uint8(sure_fg)
    # unknown = cv2.subtract(sure_bg,sure_fg)
    # plt.imshow(sure_fg,cmap = 'gray')


    plt.imshow(th4,cmap = 'gray')
    plt.title('Camera Mask'), plt.xticks([]), plt.yticks([])

    plt.show()            
