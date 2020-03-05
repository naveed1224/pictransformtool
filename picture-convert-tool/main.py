import tkinter as tk
from tkinter import filedialog
from tkinter import *
from ttkthemes import ThemedStyle
from time import sleep
from tkinter import ttk

tool = tk.Tk()

tool.title('Image Transform Tool')
tool.geometry('300x500')

#folder_selected = filedialog.askdirectory()
#from_file_btn = tk.Button(tool, text='From Folder', command=select_file)
text1 = ''
text2 = ''
E1 = ''
E2 = ''
v2 = IntVar()
v1 = IntVar()

v1.set(0)
v2.set(0)
teams = range(10)


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

def button_command():
    #start progress bar
    popup = tk.Toplevel()
    tk.Label(popup, text="Files being downloaded").grid(row=0,column=0)
    popup.geometry('150x150')
    close_button = ttk.Button(popup, text="Done", command=popup.destroy)

    progress = 0
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=100)
    progress_bar.grid(row=1, column=0)#.pack(fill=tk.X, expand=1, side=tk.BOTTOM)
    popup.pack_slaves()


    progress_step = float(100.0/len(teams))
    for team in teams:
        popup.update()
        sleep(1) # lauch task
        progress += progress_step
        progress_var.set(progress)
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
