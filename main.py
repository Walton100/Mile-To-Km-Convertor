from tkinter import *

window=Tk()

window.title('Mile To Km Convertor')
window.config(padx=20,pady=50)

window.minsize(200,200)

input=Entry(width=20)
input.grid(column=1,row=0)
mile_label=Label(text='Mile')

mile_label.grid(column=2,row=0)

is_equal_to_label=Label(text='is equal to')

is_equal_to_label.grid(column=0,row=1)

result=0

def calculate():
    global result
    miles=int(input.get())
    pre_result= miles * 1.60934
    result=round(pre_result,2)
    result_label.config(text=f'{result}')


result_label=Label(text=f'{result}')

result_label.grid(column=1,row=1)

km_label=Label(text='km')

km_label.grid(column=2,row=1)

calculate_button=Button(text='Calculate',command=calculate)

calculate_button.grid(column=1,row=2)

window.mainloop()
