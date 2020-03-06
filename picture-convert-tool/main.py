import tkinter as tk
from tkinter import filedialog
from tkinter import *
from ttkthemes import ThemedStyle
from time import sleep
from tkinter import ttk
from PIL import Image
import os, sys
from pathlib import Path
import logging

tool = tk.Tk()

tool.title('Image Transform Tool')
tool.geometry('500x700')

#folder_selected = filedialog.askdirectory()
#from_file_btn = tk.Button(tool, text='From Folder', command=select_file)
text1 = '' # from path
text2 = '' # to path
text3 = ''#picture being converted
from_file_path = ''
to_file_path = ''

E1 = '' #height
E2 = '' # width
v2 = IntVar() # zipfile selection
v1 = IntVar() # normalize selection
E3 = ''# char to replace
v1.set(0) # default as none
v2.set(0) # default as none



def from_select_file():
    from_file_path = filedialog.askdirectory()
    from_path_test_input.insert(0,from_file_path)

def to_select_file():
    to_file_path = filedialog.askdirectory()
    to_path_test_input.insert(0,to_file_path)

def button_command():
    #start progress bar
    to_path = os.path.join(Path(to_path_test_input.get()),"")
    from_path = os.path.join(Path(from_path_test_input.get()),"")

    dirs = os.listdir(from_path)

    h = int(E1.get())
    w = int(E2.get())
    var1 = int(v1.get())
    e3 = E3.get()

    Image.MAX_IMAGE_PIXELS = None

    for item in dirs:

        if os.path.isfile(os.path.join(from_path, item)):
            if item.endswith('.jpg'):
                try:
                    im = Image.open(os.path.join(from_path,item))
                    imResize = im.resize((w, h), Image.ANTIALIAS)
                    item_name = item
                    item_name = item_name.replace("{}".format(e3), "")
                    if var1 == 2:
                        item_name = item_name.lower()
                    elif var1 == 1:
                        item_name = item_name.upper()
                    else:
                        None
                    imResize.save(os.path.join(to_path,item_name), 'JPEG', quality=90)

                except ZeroDivisionError as e:
                    logging.exception("message")
        #    print('Failed')
    results.insert(0,'Done Converting pictures')




from_path_test = Label(tool, text="From Path:")
from_path_test.pack(anchor=W)
from_path_test_input = Entry(tool, bd =2, width= 60)
from_path_test_input.pack(anchor=W)
from_file_btn = tk.Button(tool, text='Select: From Folder', command=from_select_file)
from_file_btn.pack(anchor=W)

space5 = Label(tool, text=" ")
space5.pack(anchor=W)

to_path_test = Label(tool, text="To Path:")
to_path_test.pack(anchor=W)
to_path_test_input = Entry(tool, bd =2, width= 60)
to_path_test_input.pack(anchor=W)
to_file_btn = tk.Button(tool, text='Select: To Folder', command=to_select_file)
to_file_btn.pack(anchor=W)

space4 = Label(tool, text=" ")
space4.pack(anchor=W)
pic_dimen = Label(tool, text="Enter Picture Dimentions:")
pic_dimen.pack(anchor=W)

#enter height
L1 = Label(tool, text="Height")
L1.pack(anchor=W)
E1 = Entry(tool, bd =3)
E1.pack(anchor=W)


#enter Width
L2 = Label(tool, text="Width")
L2.pack(anchor=W)
E2 = Entry(tool, bd =3)
E2.pack(anchor=W)

space3 = Label(tool, text=" ")
space3.pack(anchor=W)

text3 = tk.Label(tool, text='Normalize Names options:')
text3.pack(anchor=W)
Radiobutton(tool, text="None", variable=v1, value=0).pack(anchor=W)
Radiobutton(tool, text="Capitalize Names", variable=v1, value=1).pack(anchor=W)
Radiobutton(tool, text="LowerCase Names", variable=v1, value=2).pack(anchor=W)

space2 = Label(tool, text=" ")
space2.pack(anchor=W)

L3 = Label(tool, text="Enter Text to replace(default: None):")
L3.pack(anchor=W)
E3 = Entry(tool, bd =2, width= 60)
E3.pack(anchor=W)


space1 = Label(tool, text=" ")
space1.pack(anchor=W)
text4 = tk.Label(tool, text='Create and Zip pictures in a zipped folder:')
text4.pack(anchor=W)
Radiobutton(tool, text="No", variable=v2, value=0).pack(anchor=W)
Radiobutton(tool, text="Yes", variable=v2, value=1).pack(anchor=W)



Start_process = tk.Button(tool, text='Start Conversion', command=button_command)
Start_process.pack()

tk.Label(tool, text="Pictures Status():").pack(anchor=W)
#    text3 = tk.Label(popup, text="----").grid(row=2, column=0)
results = Entry(tool, bd =2, width= 60)
results.pack(anchor=W)

space = Label(tool, text=" ")
space.pack(anchor=W)

copyright = Label(tool, text="Only use for Internal Loblaw use - Developed by Naveed Sultan")
copyright.pack(anchor=W)

tool.mainloop()
