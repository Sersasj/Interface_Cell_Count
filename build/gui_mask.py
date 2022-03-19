
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import threading

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scale, ttk, Menu, IntVar, StringVar, Label
from tkinter.filedialog import askopenfilenames
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("194x376")
window.configure(bg = "#FFFFFF")



#---------------------------------Var-------------------------------------------------#
img_list = []
img_list_all = []
img_list_mono = []
img_list_mono_bi = [] 
pen_color = StringVar("")
i = IntVar(0)
pen_color = StringVar("")
save_path = StringVar("")


pen_color = [(37, 215, 249),(117, 228, 43),(228, 61, 43)]
color_index = IntVar(0)
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 376,
    width = 194,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    194.0,
    376.0,
    fill="#FCBDBD",
    outline="")

button_image_eraser = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_eraser = Button(
    image=button_image_eraser,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_eraser.place(
    x=7.0,
    y=54.0,
    width=44.0,
    height=33.0
)

button_image_bi = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_bi = Button(
    image=button_image_bi,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: color_index.set(1),
    relief="flat"
)
button_bi.place(
    x=7.0,
    y=118.0,
    width=44.0,
    height=33.0
)

button_image_kup = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_kup = Button(
    image=button_image_kup,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: color_index.set(2),
    relief="flat"
)
button_kup.place(
    x=7.0,
    y=151.0,
    width=44.0,
    height=33.0
)

canvas.create_text(
    67.0,
    61.0,
    anchor="nw",
    text="Borracha",
    fill="#000000",
    font=("Roboto", 18 * -1)
)

canvas.create_text(
    66.0,
    93.0,
    anchor="nw",
    text="Mononucleado",
    fill="#000000",
    font=("Roboto", 18 * -1)
)

canvas.create_text(
    67.0,
    125.0,
    anchor="nw",
    text="Binucleado",
    fill="#000000",
    font=("Roboto", 18 * -1)
)

button_image_save = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_save = Button(
    image=button_image_save,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_save.place(
    x=0.0,
    y=276.0,
    width=194.0,
    height=30.0
)

button_image_right = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_right = Button(
    image=button_image_right,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_img_right(),
    relief="flat"
)
button_right.place(
    x=97.0,
    y=344.0,
    width=97.0,
    height=32.0
)

button_image_left = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_left = Button(
    image=button_image_left,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_img_left(),
    relief="flat"
)
button_left.place(
    x=0.0,
    y=344.0,
    width=97.0,
    height=32.0
)

button_image_mono = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_mono = Button(
    image=button_image_mono,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: color_index.set(0),
    relief="flat"
)
button_mono.place(
    x=7.0,
    y=87.0,
    width=44.0,
    height=33.0
)

canvas.create_text(
    66.0,
    158.0,
    anchor="nw",
    text="Kupffer",
    fill="#000000",
    font=("Roboto", 18 * -1)
)

canvas.create_rectangle(
    0.0,
    206.0,
    194.0,
    276.0,
    fill="#F6F3F3",
    outline="")

canvas.create_text(
    7.0,
    206.0,
    anchor="nw",
    text="Tam",
    fill="#000000",
    font=("Roboto", 18 * -1)
)



#------------------------------------------Feito Manual----------------------------------------#

window.wm_title("Mask_Maker")


menu_bar = Menu(window)
help_menu = Menu(menu_bar,tearoff=False)
file_menu = Menu(menu_bar,tearoff=False)
menu_bar.add_cascade(label="Selecionar", menu=file_menu)

file_menu.add_command(label='Selecionar Imagens', 
                      command=lambda: [img_list.clear(),
                      img_list_all.clear(),
                      img_list_mono.clear(),
                      img_list_mono_bi.clear(),
                      select_images(), 
                      i.set(0),
                      update_image(),
                      
                      cv.namedWindow(winname='meu_desenho'),
                      cv.setMouseCallback('meu_desenho', desenho_livre)])
window.config(menu=menu_bar)
                          
pen_size = Scale(
    orient="horizontal",
    from_ = 0,
    to = 50,
    length = 80
)
pen_size.place(
    x = 0,
    y = 225,
    width = 170
)      
pen_size.set(5)





desenho = False


#funcoes
def desenho_livre(evento,x,y,flags,param):

    global ix, iy, desenho
    
    if evento == cv.EVENT_LBUTTONDOWN:
        desenho = True
        ix = x
        iy = y

    elif evento == cv.EVENT_MOUSEMOVE:
        print(color_index.get(), pen_color[color_index.get()] )

        if desenho == True:
            cv.line(img_list[i.get()], (ix,iy), (x,y), pen_color[color_index.get()], pen_size.get())
            
            if(color_index.get() == 0):
                cv.line(img_list_all[i.get()], (ix,iy), (x,y), (1,1,1), pen_size.get())
                cv.line(img_list_mono[i.get()], (ix,iy), (x,y), (1,1,1), pen_size.get())
                cv.line(img_list_mono_bi[i.get()], (ix,iy), (x,y), (1,1,1), pen_size.get())
            if(color_index.get() == 1):
                cv.line(img_list_all[i.get()], (ix,iy), (x,y), (2,2,2), pen_size.get())
                #cv.line(img_list_mono[i.get()], (ix,iy), (x,y), (2,2,2), pen_size.get())
                cv.line(img_list_mono_bi[i.get()], (ix,iy), (x,y), (2,2,2), pen_size.get())                
            if(color_index.get() == 2):
                cv.line(img_list_all[i.get()], (ix,iy), (x,y), (3,3,3), pen_size.get())
                #cv.line(img_list_mono[i.get()], (ix,iy), (x,y), (2,2,2), pen_size.get())
                #cv.line(img_list_mono_bi[i.get()], (ix,iy), (x,y), (3,3,3), pen_size.get())                
                                
            # faz a elipse
            #ix, iy = x, y
            

    elif evento == cv.EVENT_LBUTTONUP:
        print(color_index.get(), pen_color[color_index.get()] )

        desenho = False
        cv.line(img_list[i.get()], (ix,iy), (x,y), pen_color[color_index.get()], pen_size.get())
        
        if(color_index.get() == 0):
            cv.line(img_list_all[i.get()], (ix,iy), (x,y), (1,1,1), pen_size.get())
            cv.line(img_list_mono[i.get()], (ix,iy), (x,y), (1,1,1), pen_size.get())
            cv.line(img_list_mono_bi[i.get()], (ix,iy), (x,y), (1,1,1), pen_size.get())
        if(color_index.get() == 1):
            cv.line(img_list_all[i.get()], (ix,iy), (x,y), (2,2,2), pen_size.get())
            #cv.line(img_list_mono[i.get()], (ix,iy), (x,y), (2,2,2), pen_size.get())
            cv.line(img_list_mono_bi[i.get()], (ix,iy), (x,y), (2,2,2), pen_size.get())                
        if(color_index.get() == 2):
            cv.line(img_list_all[i.get()], (ix,iy), (x,y), (3,3,3), pen_size.get())
            #cv.line(img_list_mono[i.get()], (ix,iy), (x,y), (2,2,2), pen_size.get())
            #cv.line(img_list_mono_bi[i.get()], (ix,iy), (x,y), (3,3,3), pen_size.get()) 
    update_image()    



def update_image():
    
    if img_list == []:
        return

    cv.imshow('meu_desenho', img_list[i.get()])

    k = cv.waitKey(1)
       
    if k == 27: # tecla Esc
        cv.destroyAllWindows()
    
    #cv.destroyAllWindows()

def change_img_right():
    if i.get() >= len(img_list)-1:

        return
    else:
        i.set(i.get()+1) 
    
    update_image()     

def change_img_left():
    if i.get() <= 0:
        return
    else:
        i.set(i.get()-1)
    update_image()     



def select_images():
    filenames = askopenfilenames(title="Choose a file",
        filetypes=[('image files', ('.png', '.jpg', '.jfif'))])
    
    for file in filenames:
        img = cv.imread(file)
        #img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        height, width, a = img.shape
        aux = np.zeros_like(img)        
        img_list.append(img)
        img_list_all.append(aux) #
        img_list_mono.append(aux)
        img_list_mono_bi.append(aux)
        
   
window.resizable(False, False)
window.mainloop()