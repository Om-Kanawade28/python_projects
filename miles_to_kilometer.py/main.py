from tkinter import *

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

window = Tk()
window.title("demo")
window.geometry("300x200")

# Title
title_label = Label(master=window, text="Miles to Kilometers", font="Arial 18 bold")
title_label.pack()

# Input
input_frame = Frame(master=window)
entry_int = IntVar()
entry = Entry(master=input_frame, textvariable=entry_int)
button = Button(master=input_frame, text='Convert', command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

# Output1
output_string = StringVar()
output_label = Label(master=window, text='Output', font='Arial 12 bold', textvariable=output_string)
output_label.pack()

window.mainloop()
