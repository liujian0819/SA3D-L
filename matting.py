 
import cv2
import numpy as np
file1="E:\\Nerf\\nerf-pytorch\\data\\images5\\002.png"
file2="E:\\Nerf\\nerf-pytorch\\data\\images5\\003.png"
images_bk=cv2.imread(file1,-1)
images_mask=cv2.imread(file2,-1)

h,w,c=images_bk.shape
images_white=np.ones((h,w,c))*255
for i in range(h):
                    for j in range(w):
                        if(images_mask[i,j,1]>=200):
                            images_bk[i,j]=images_mask[i,j]

cv2.imwrite(file1,images_bk)
                          
                          

                       
                       