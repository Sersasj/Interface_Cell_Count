# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:12:55 2021

@author: sergi
"""

import skimage.morphology as mm
import PySimpleGUI as sg
import numpy as np
import cv2 as cv

def frame(a,tipo):
    z = np.zeros(a.shape,dtype=tipo)
    if tipo == 'bool':
        z[0,:] = True
        z[-1,:] = True
        z[:,0] = True
        z[:,-1] = True
    else:
        z[0,:] = 1
        z[-1,:] = 1
        z[:,0] = 1
        z[:,-1] = 1        
    return z

def fechaburacos(a,Bc):
    aneg = 255 - a
    f = 255*frame(a,'uint8')
    f = np.minimum(f,aneg)
    abe = 255 - mm.reconstruction(f,aneg,selem=Bc)
    return abe

def visualiza(a,b):
    # Cria as bandas coloridas
    ar = a.copy()
    ag = a.copy()
    ab = a.copy()
    b2 = mm.dilation(b) - mm.erosion(b)
    # Atribui a cor vermelha às bandas
    ar[b2>0] = 255
    ag[b2>0] = 0
    ab[b2>0] = 0
    # Junta as bandas
    return np.dstack((np.dstack((ab,ag)),ar))

def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Button("Cinza"),
            sg.Button("Binario"),
            sg.Button("WaterShed"),
            sg.Button("Bordas"),
            sg.Button("Celula"),
        ],
    ]
    window = sg.Window("Image Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "Cinza":
            image = cv.imread('1.jpg')
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            cv.imshow("Imagem_cinza",image)

        if event == "Bordas":
            a = cv.imread('2.jpg',0)
            B = mm.disk(20)
            B2 = mm.disk(5)
            Bc = np.array([[0,1,0],[1,1,1],[0,1,0]])
            #1
            op1 = mm.dilation(a,selem=B)
            op1 = np.int32(mm.reconstruction(op1,a, method='erosion', selem=Bc))
            op1 = np.uint8(op1)
            #2
            op2 = mm.dilation(a,selem=B2)
            op2 = np.int32(mm.reconstruction(op2,a, method='erosion', selem=Bc))
            op2 = np.uint8(op2)
            # 3
            op3 = op1 - op2
            # 4
            op4 = op3 >= 20
            op4 = np.uint8(255*op4)
            # 5
            op5 = fechaburacos(op4,Bc)
            
            cv.imshow('visualiza',visualiza(a, op5))

        if event == "Binario":
            image = cv.imread("1.jpg")
            canal_verde = image[:,:,1]
            _,binario = cv.threshold(canal_verde, 160, 255, cv.THRESH_BINARY)
            cv.imshow("Binario",binario)

        if event == "Celula":
            a = cv.imread('1.jpg',0)
            imagem = cv.imread('1.jpg')
            B = mm.disk(10)
            B2 = mm.disk(5)
            Bc = np.array([[0,1,0],[1,1,1],[0,1,0]])
            # 1
            op1 = mm.dilation(a,selem=B)
            op1 = np.int32(mm.reconstruction(op1,a, method='erosion', selem=Bc))
            op1 = np.uint8(op1)
            # 2
            op2 = mm.dilation(a,selem=B2)
            op2 = np.int32(mm.reconstruction(op2,a, method='erosion', selem=Bc))
            op2 = np.uint8(op2)
            # 3
            op3 = op1 - op2
            # 4
            op4 = op3 >= 20
            op4 = np.uint8(255*op4)
            # 5
            op5 = fechaburacos(op4,Bc)
            #CONTORNO
            fonte = cv.FONT_ITALIC
            contorno,hierarquia = cv.findContours(op4,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
            for (i,c) in enumerate(contorno):
                if hierarquia[0][i][3] == -1:
                    ((x,y),_) = cv.minEnclosingCircle(c)
                    #cv.drawContours(imagem,contorno,i,(0,255,255),2)
                    cv.putText(imagem, text='{}'.format(i+1), org=(int(x) - 10,int(y)), fontFace=fonte, fontScale=0.6, color=(0,255,0), thickness=2, lineType=cv.LINE_4);
            
            cv.imshow('CONTORNO', imagem)
            

    window.close()


if __name__ == "__main__":
    main()