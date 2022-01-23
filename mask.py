# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:23:43 2022

@author: sergi
"""

import cv2 as cv

import numpy as  np
import cv2 as cv
from skimage.segmentation import watershed
import skimage.morphology as mm

desenho = False

ix = -1
iy = -1

troca_cor = 1
tam_bola = 20
linha_colorida = [(0,255,255),(255,255,0),(0,255,0),(0,0,255),(205,90,106),
                  (0,255,127),(30,105,210),(130,0,75),(255,0,255),(255,0,0)]

linha_cinza = [(0,0,0),(0,0,0)]

img = cv.imread('2.jpg')

img_c = cv.imread('1.jpg',0)


img_copia = img.copy()

fundo_branco = np.zeros(img.shape[:2],dtype=np.int32)
fundo_branco.fill(255)

def desenho_livre(evento,x,y,flags,param):

    global ix, iy, desenho
    
    if evento == cv.EVENT_LBUTTONDOWN:
        desenho = True
        ix = x
        iy = y

    elif evento == cv.EVENT_MOUSEMOVE:
        
        if desenho == True:
            cv.line(img_copia, (ix,iy), (x,y), linha_colorida[troca_cor], 6)
            cv.line(fundo_branco, (ix,iy), (x,y), linha_cinza[troca_cor], 6)
            # faz a elipse
            #ix, iy = x, y
            

    elif evento == cv.EVENT_LBUTTONUP:
        desenho = False
        cv.line(img_copia, (ix,iy), (x,y), linha_colorida[troca_cor], 6)
        cv.line(fundo_branco, (ix,iy), (x,y), linha_cinza[troca_cor], 6)

    elif evento == cv.EVENT_RBUTTONDOWN:
        cv.circle(img_copia,(x,y),tam_bola,linha_colorida[troca_cor],thickness=-1)
        cv.circle(fundo_branco,(x,y),tam_bola,linha_cinza[troca_cor],thickness=-1)

cv.namedWindow(winname='meu_desenho')

cv.setMouseCallback('meu_desenho', desenho_livre)

while True:
    
    cv.imshow('meu_desenho', img_copia)

    k = cv.waitKey(1)
       
    if k == 27: # tecla Esc
        break

    elif k == ord('s'):
        cv.imwrite('2_mask.jpg', fundo_branco)

    elif k == ord('='):
        tam_bola+=1   
    elif k == ord('-'):
        tam_bola-=1      
        

        
    elif k > 0 and chr(k).isdigit():
        troca_cor = int(chr(k))
        
            
cv.destroyAllWindows()

# 8 conexo connectivity = 2
# 4 conexo connectivity = 1 