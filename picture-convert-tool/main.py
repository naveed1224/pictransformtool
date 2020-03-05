import tkinter as tk
from tkinter import filedialog
from tkinter import *

tool = tk.Tk()

tool.title('Image Transform Tool')

#folder_selected = filedialog.askdirectory()
#from_file_btn = tk.Button(tool, text='From Folder', command=select_file)
text1 = ''
text2 = ''
E1 = ''
E2 = ''


def from_select_file():
    from_file_path = filedialog.askdirectory()
    text1.config(text=from_file_path)

def to_select_file():
    to_file_path = filedialog.askdirectory()
    text2.config(text=to_file_path)

def print_num():
    print(E1.get())
    print(E2.get())


text1 = tk.Label(tool, text='----')
from_file_btn = tk.Button(tool, text='Select: From Folder', command=from_select_file)

text2 = tk.Label(tool, text='----')
to_file_btn = tk.Button(tool, text='Select: To Folder', command=to_select_file)



text1.pack()
from_file_btn.pack()

text2.pack()
to_file_btn.pack()
#enter height
L1 = Label(tool, text="Height")
L1.pack()
E1 = Entry(tool, bd =2)
E1.pack()


#enter Width
L2 = Label(tool, text="Width")
L2.pack()
E2 = Entry(tool, bd =6)
E2.pack()


print_num1 = tk.Button(tool, text='print numbers', command=print_num)

print_num1.pack()
tool.mainloop()
