import tkinter as tk
from tkinter import filedialog
from tkinter import *
from ttkthemes import ThemedStyle
from time import sleep
from tkinter import ttk
from PIL import Image
import os, sys
from pathlib import Path

tool = tk.Tk()

tool.title('Image Transform Tool')
tool.geometry('300x500')

#folder_selected = filedialog.askdirectory()
#from_file_btn = tk.Button(tool, text='From Folder', command=select_file)
text1 = '' # from path
text2 = '' # to path
text3 = ''#picture being converted
from_file_path1 = ''
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
    text1.config(text=from_file_path)

def to_select_file():
    to_file_path = filedialog.askdirectory()
    text2.config(text=to_file_path)

def print_num():
    print(E1.get())
    print(E2.get())


def radio_button_output():
    print(v1.get())
    print(v2.get())
    print(text1)
    print('hello')

def button_command():
    #start progress bar
    print(from_file_path)
    from_path = Path(from_file_path)
    to_path = Path(to_file_path)
    print(from_path)
    print('hello')

    popup = tk.Toplevel()
    tk.Label(popup, text="Following Pictures are beoing converted:").grid(row=0,column=0)
    text3 = tk.Label(popup, text="----").grid(row=2, column=0)
    popup.geometry('200x200')
    dirs = os.listdir(from_path)
    h = int(E1.get())
    w = int(E2.get())
    Image.MAX_IMAGE_PIXELS = None

    for item in dirs:
        if os.path.isfile(from_path + item):
            im = Image.open(from_path + item)
            imResize = im.resize((w, h), Image.ANTIALIAS)
            item_name = item
            item_name = item_name.replace("{}".format(E3), "")
            if v1 == 1:
                item_name = item_name.lower()
            elif v1 == 2:
                item_name = item_name.upper()
            else:
                None
            imResize.save(to_path + item_name, 'JPEG', quality=90)
            text3.config(text=item_name)

        #    print('Failed')
    popup.destroy()




text1 = tk.Label(tool, text='----')
from_file_btn = tk.Button(tool, text='Select: From Folder', command=from_select_file)

text2 = tk.Label(tool, text='----')
to_file_btn = tk.Button(tool, text='Select: To Folder', command=to_select_file)



text1.pack(anchor=W)
from_file_btn.pack(anchor=W)

text2.pack(anchor=W)
to_file_btn.pack(anchor=W)
#enter height
L1 = Label(tool, text="Height")
L1.pack(anchor=W)
E1 = Entry(tool, bd =2)
E1.pack(anchor=W)


#enter Width
L2 = Label(tool, text="Width")
L2.pack(anchor=W)
E2 = Entry(tool, bd =6)
E2.pack(anchor=W)


print_num1 = tk.Button(tool, text='print numbers', command=print_num)

print_num1.pack(anchor=W)


text3 = tk.Label(tool, text='Normalize Names options:')
text3.pack(anchor=W)
Radiobutton(tool, text="None", variable=v1, value=0).pack(anchor=W)
Radiobutton(tool, text="Capitalize Names", variable=v1, value=1).pack(anchor=W)
Radiobutton(tool, text="LowerCase Names", variable=v1, value=2).pack(anchor=W)

L3 = Label(tool, text="Enter Text to replace(default: None):")
L3.pack(anchor=W)
E3 = Entry(tool, bd =2)
E3.pack(anchor=W)



text4 = tk.Label(tool, text='Create and Zip pictures in a zipped folder:')
text4.pack(anchor=W)
Radiobutton(tool, text="No", variable=v2, value=0).pack(anchor=W)
Radiobutton(tool, text="Yes", variable=v2, value=1).pack(anchor=W)



Start_process = tk.Button(tool, text='Start Conversion', command=button_command)
Start_process.pack()
tool.mainloop()
