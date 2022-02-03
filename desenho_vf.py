import numpy as  np
import cv2 as cv
from skimage.segmentation import watershed
import skimage.morphology as mm
import math as mt

desenho = False
linha = False
circ = False
livre = False
borracha = False

ix = -1
iy = -1

jx = -1
jy = -1

kx = -1
ky = -1

troca_cor = 1

linha_colorida = [(0,255,255),(255,255,0),(0,255,0),(0,0,255),(205,90,106),
                  (0,255,127),(30,105,210),(130,0,75),(255,0,255),(255,0,0)]

linha_cinza = [(128,128,128),(79,79,79),(192,192,192),(169,169,169),(220,220,220),
               (255,255,255),(119,136,153),(47,79,79),(211,211,211),(105,105,105)]

point = list()

img = cv.imread('controle (45).jpg')

img_c = img.copy()

def clear(x,y,jx,jy):
    for coluna in range(x,jx+1,1):
        for linha in range(y,jy+1,1):
            if img[linha,coluna,0] != img_c[linha,coluna,0] and img[linha,coluna,1] != img_c[linha,coluna,1] and img[linha,coluna,2] != img_c[linha,coluna,2]:
                img[linha,coluna,0] = img_c[linha,coluna,0]
                img[linha,coluna,1] = img_c[linha,coluna,1]
                img[linha,coluna,2] = img_c[linha,coluna,2]

def raio(x,y,kx,ky):
    return int(mt.sqrt((x - kx)**2 + (y - ky)**2))

def desenho_livre(evento,x,y,flags,param):

    global ix, iy, desenho, livre, linha, circ, jx, jy, borracha, kx, ky

            ########## DESENHO LIVRE ##########
    
    if evento == cv.EVENT_LBUTTONDOWN:
        desenho = True
        ix = x 
        iy = y

    elif evento == cv.EVENT_MOUSEMOVE:
        if desenho == True and livre == True:
            cv.line(img, (ix,iy), (x,y), linha_colorida[troca_cor], 2)
            ix, iy = x, y
        
    elif evento == cv.EVENT_LBUTTONUP and livre == True:
        desenho = False
        cv.line(img, (ix,iy), (x,y), linha_colorida[troca_cor], 2)

            ########## CIRCUNFERêNCIA ##########

    if evento == cv.EVENT_LBUTTONDOWN and circ == True:
        kx, ky = x, y

    elif evento == cv.EVENT_LBUTTONUP and circ == True:
        cv.circle(img,(kx,ky),raio(x,y,kx,ky),(0,255,0),thickness=1)
        cv.circle(img,(kx,ky),1,(255,0,0),thickness=-1)
        
            ########## LINHA ##########
        
    if evento == cv.EVENT_LBUTTONDOWN and linha == True:
        point.append((x,y))
        cv.circle(img,(x,y),2,(0,0,255),thickness=-1)
        if len(point) % 2 == 0:
            cv.line(img, point[0], point[1],(0,255,0), 2)
            cv.circle(img,point[1],2,(0,0,255),thickness=-1)
            point.clear()

            ########## BORRACHA ##########

    if evento == cv.EVENT_LBUTTONDOWN and borracha == True:
        jx,jy = x,y

    elif evento == cv.EVENT_LBUTTONUP and borracha == True:
        #cv.rectangle(img_copia,(jx,jy),(x,y),(0,255,0),1)
        clear(jx,jy,x,y)
        clear(x,y,jx,jy)
    

cv.namedWindow(winname='meu_desenho')

cv.setMouseCallback('meu_desenho', desenho_livre)

while True:
    
    cv.imshow('meu_desenho', img)

    k = cv.waitKey(1)
       
    if k == ord('x') or k == ord('X'):
        print('PROGRAMA FINALIZADO')
        break

    elif k == 27:
        print('ESPERANDO COMANDO...')
        circ = False
        linha = False
        livre = False
        desenho = False
        borracha = False
        
    elif k > 0 and chr(k).isdigit():
        troca_cor = int(chr(k))

    elif k == ord('l') or k == ord('L'):
        print('LINHA')
        linha = True
        circ = False
        livre = False
        borracha = False

    elif k == ord('c') or k == ord('C'):
        print('CIRCUNFERêNCIA')
        circ = True
        linha = False
        livre = False
        borracha = False

    elif k == ord('w') or k == ord('W'):
        print('DESENHO LIVRE')
        circ = False
        linha = False
        livre = True
        borracha = False

    elif k == ord('b') or k == ord('B'):
        print('BORRACHA')
        circ = False
        linha = False
        livre = False
        borracha = True
            
cv.destroyAllWindows()


# 8 conexo connectivity = 2
# 4 conexo connectivity = 1
