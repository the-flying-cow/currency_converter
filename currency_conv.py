import tkinter as tk
from tkinter import *

win = Tk()
win.title('Currency-Converter')

center_frame = Frame(win,bg='grey',width=500,height=500)
center_frame.pack(expand=True)
center_frame.pack_propagate(False)

label = Label(center_frame,text='Currency Converter',bg='sky blue',font=('TkDefaultFont', 12),justify=CENTER)
label.pack(pady=10)
label.pack_propagate(False)

result_frame = Frame(center_frame,border=10,bg='red',height=45,width=350)
result_frame.pack(expand=False)
result_frame.pack_propagate(False)

win.mainloop()