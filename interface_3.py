# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 11:39:13 2021

@author: FMate
"""

import PySimpleGUI as sg
import cv2
import numpy as np


sg.theme("LightGreen")

    # Define the window layout
layout = [
        [sg.Text("OpenCV Demo", size=(60, 1), justification="center")],
        [sg.Image(filename="", key="-IMAGE-")],
        [sg.Radio("None", "Radio", True, size=(10, 1))],
        [
            sg.Radio("threshold", "Radio", size=(10, 1), key="-THRESH-"),
            sg.Slider(
                (0, 255),
                128,
                1,
                orientation="h",
                size=(40, 15),
                key="-THRESH SLIDER-",
            ),
        ],
        [
            sg.Radio("canny", "Radio", size=(10, 1), key="-CANNY-"),
            sg.Slider(
                (0, 255),
                128,
                1,
                orientation="h",
                size=(20, 15),
                key="-CANNY SLIDER A-",
            ),
            sg.Slider(
                (0, 255),
                128,
                1,
                orientation="h",
                size=(20, 15),
                key="-CANNY SLIDER B-",
            ),
        ],
        [
            sg.Radio("blur", "Radio", size=(10, 1), key="-BLUR-"),
            sg.Slider(
                (1, 11),
                1,
                1,
                orientation="h",
                size=(40, 15),
                key="-BLUR SLIDER-",
            ),
        ],
        [
            sg.Radio("hue", "Radio", size=(10, 1), key="-HUE-"),
            sg.Slider(
                (0, 225),
                0,
                1,
                orientation="h",
                size=(40, 15),
                key="-HUE SLIDER-",
            ),
        ],
        [
            sg.Radio("enhance", "Radio", size=(10, 1), key="-ENHANCE-"),
            sg.Slider(
                (1, 255),
                200,
                1,
                orientation="h",
                size=(40, 15),
                key="-ENHANCE SLIDER-",
            ),
        ],
        [sg.Button("Exit", size=(10, 1))],
]

# Create the window and show it without the plot
window = sg.Window("OpenCV Integration", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    frame = cv2.imread("mateus filipe tavares carvalho.png")
    
    if values["-THRESH-"]:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)[:, :, 0]
        frame = cv2.threshold(frame, values["-THRESH SLIDER-"], 255, cv2.THRESH_BINARY)[1]
    elif values["-CANNY-"]:
        frame = cv2.Canny(
        frame, values["-CANNY SLIDER A-"], values["-CANNY SLIDER B-"])
    elif values["-BLUR-"]:
        frame = cv2.GaussianBlur(frame, (21, 21), values["-BLUR SLIDER-"])
    elif values["-HUE-"]:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame[:, :, 0] += int(values["-HUE SLIDER-"])
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

    
    window["-IMAGE-"].update(data=imgbytes)

window.close()
