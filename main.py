from genericpath import isfile
import tensorflow
import cv2
import os
import numpy as np
from tqdm import tqdm
import shutil
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import align_image
import crop_image

def align_crop_resize(source_dir, dest_dir,height,width):
    aligned_dir = os.path.join(dest_dir, 'Aligned Images')
    cropped_dir =os.path.join(dest_dir, 'Cropped Image')
    if os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    os.mkdir(aligned_dir)
    os.mkdir(cropped_dir)
    image_list =os.listdir(source_dir)
    success_count=0
    for i,file in enumerate(image_list):
         image_name=os.path.join(source_dir,file)
         if os.path.isfile(image_name):
            try:
                img=cv2.imread(image_name)
                shape=img.shape

                status, img = align_image.align_image(img)
                if status:
                    aligned_path=os.path.join(aligned_dir,file)
                    cv2.imwrite(aligned_path, img)
                    cstatus, img=crop_image.crop_image(img)
                    if cstatus:
                        img=cv2.resize(img, (height, width))
                    cropped_path=os.path.join(cropped_dir, file)
                    cv2.imwrite(cropped_path, img)
                    success_count +=1
            except:
                print('file', image_name ,'is a bad file')
    return success_count


         

source_dir='all_images'
dest_dir='datasets'
height=200
width=200
count=align_crop_resize(source_dir,dest_dir,height,width)
print ('Number of sucessfully processed images= ', count)
