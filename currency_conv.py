import tkinter as tk
from tkinter import *
from tkinter import ttk

win = Tk()
win.title('Currency-Converter')

center_frame = Frame(win,bg='grey',width=400,height=400,relief=RIDGE,borderwidth=5)
center_frame.pack(expand=True)
center_frame.pack_propagate(False)

label = Label(center_frame,text='Currency-Converter',bg='sky blue',font=('TkDefaultFont', 12),justify=CENTER,relief=RAISED)
label.pack(pady=10)
label.pack_propagate(False)

def option_validate():
    print('hello')

from_frame = Frame(center_frame,border=10,bg='light grey',height=45,width=350)
from_frame.pack(expand=False,pady=10)
from_frame.pack_propagate(False)
from_label = Label(from_frame,text='FROM :',bg='sky blue',border=5,relief=FLAT,font=('Arial', 10))
from_label.pack(expand=True)
from_label.pack_propagate(False)
from_label.place(x=-5)

from_box = ttk.Combobox(from_frame,values=['INR','DOLLAR','POUND'])
from_box.pack(expand=True)
from_box.pack_propagate(False)

to_frame = Frame(center_frame,border=10,bg='light grey',height=45,width=350)
to_frame.pack(expand=False,pady=20)
to_frame.pack_propagate(False)
to_label = Label(to_frame,text='TO :',bg='sky blue',border=5,relief=FLAT,font=('Arial', 10))
to_label.pack(expand=True)
to_label.pack_propagate(False)
to_label.place(x=-5)

to_box = ttk.Combobox(to_frame,values=['INR','DOLLAR','POUND'])
to_box.pack(expand=True)
to_box.pack_propagate(False)

convert_button = Button(center_frame,text='CONVERT',bg='red',width=10,height=1)
convert_button.pack(expand=True)
convert_button.pack_propagate(False)


win.mainloop()