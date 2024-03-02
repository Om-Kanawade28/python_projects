import tkinter as tk
from tkinter import ttk 
def function():
    print("click button")
window = tk.Tk()
window.title('text and button')
window.geometry('800x500')
#widghit
label = ttk.Label(master=window,text='this is test')
label.pack()
text = tk.Text(master=window)
text.pack()
entry = ttk.Entry(master= window)
entry.pack()
button = ttk.Button(master=window,text='A Button',command=function)
button.pack()
#run
window.mainloop()