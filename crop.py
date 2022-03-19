# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:25:32 2022

@author: sergi
"""
import glob
import cv2 as cv
from PIL import Image
from matplotlib import pyplot as plt


#plt.imshow('1.jpg',)

img100 = cv.imread('0.png',0)
"""
#tranforma em grayscale
aux = 1
for img_path in glob.glob("Original/label/*.jpg"):

    img = cv.imread(img_path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    for i in range(768):
        for j in range(1024):
            if gray[i,j] < 20:
                gray[i,j] = 0
            else:
                gray[i,j] = 255
    cv.imwrite(str(aux)+".jpg",gray )         
    print("ao")
    aux += 1          
 
   
"""
"""
#tranforma 1 imagem 1024x768 em 12 imagens 256x256
aux = 1    
for img_path in glob.glob("Original/label_cinza/*.jpg"):    
    img = cv.imread(img_path,0)
    for i in range(0,768,256):
        for j in range(0,1024,256):           
            
            cv.imwrite(str(aux)+".jpg", img[i:i+256,j:j+256])
            aux +=1
"""
"""
aux = 1
img = cv.imread('24.jpg')
for i in range(0,768,256):
    for j in range(0,1024,256):           
        
        cv.imwrite(str(aux)+".jpg", img[i:i+256,j:j+256])
        aux +=1
  


aux = 1    
for img_path in glob.glob("img_augmented/aug_mask/*.jpg"):    
    img = cv.imread(img_path)
    for i in img:
        for j in img:           
            img[i/j] = 1 - int(img[i,j]/255)
    cv.imwrite(str(aux)+".jpg", img)        
    aux +=1  
"""       

    
    