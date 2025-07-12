import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Currency-Converter')

center_frame = tk.Frame(win,bg='grey',width=400,height=400,relief=tk.RIDGE,borderwidth=5)
center_frame.pack(expand=True)
center_frame.pack_propagate(False)

label = tk.Label(center_frame,text='Currency-Converter',bg='sky blue',font=('TkDefaultFont', 12),justify=tk.CENTER,relief=tk.RAISED)
label.pack(pady=10)

result_label = tk.Label(center_frame,text='RESULT WILL BE SHOWN HERE',height=1,width=26,relief=tk.RIDGE)
result_label.place(x=100,y=276)

def exchange():
    value = text_box.get()
    from_value = from_box.get()
    to_value = to_box.get()

    try:
        from_amount = float(value)

        rates_dict = {'INR':{'USD': 0.012, 'GBP': 0.0095, 'INR': 1},
                  'USD':{'INR': 83.33, 'GBP': 0.79, 'USD': 1},
                  'GBP':{'INR': 105.26, 'USD': 1.26, 'GBP': 1}}
        
        rate = rates_dict[from_value][to_value]
        to_amount = rate*from_amount

        result_label.config(text=f"{to_amount:.3f}")

    except:
        result_label.config(text='Please input valid numerical values')

from_frame = tk.Frame(center_frame,border=10,bg='light grey',height=45,width=350)
from_frame.pack(expand=False,pady=10)
from_frame.pack_propagate(False)
from_label = tk.Label(from_frame,text='FROM :',bg='sky blue',border=5,relief=tk.FLAT,font=('Arial', 10))
from_label.place(x=-5)
from_box = ttk.Combobox(from_frame,values=['INR','USD','GBP'])
from_box.place(x=190)

to_frame = tk.Frame(center_frame,border=10,bg='light grey',height=45,width=350)
to_frame.pack(expand=False,pady=20)
to_frame.pack_propagate(False)
to_label = tk.Label(to_frame,text='TO :',bg='sky blue',border=5,relief=tk.FLAT,font=('Arial', 10))
to_label.place(x=-5)
to_box = ttk.Combobox(to_frame,values=['INR','USD','GBP'])
to_box.place(x=190)

#default selection
from_box.set('INR')
to_box.set('USD')

text_box = tk.Entry(center_frame,bg='yellow',border=5,relief=tk.RIDGE,font=('TkDefaultFont', 12))
text_box.pack(expand=True)

convert_button = tk.Button(center_frame,text='CONVERT',bg='red',width=10,height=1,command=exchange)
convert_button.pack(expand=True)

win.mainloop()