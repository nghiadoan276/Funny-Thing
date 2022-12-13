from tkinter import *
from tkinter.ttk import *
from time import strftime

root =  Tk()
root.title('Nghiax clock')
def clock():
    string = strftime('%H:%M:%S:%p')
    label.config(text = string)
    label.after(1000,clock)
    
label = Label(root,font = ('digital-7',100),background='black',foreground='green')
label.pack(anchor='center')
clock()
root.mainloop()