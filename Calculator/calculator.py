from tkinter import *

root =Tk()
root.title("Simple Calculator")
root.geometry("500x700")

def calculate():
    result = eval(entry.get())
    result_label.config(text="Result: " + str(result))

entry =Entry(root, width=20)
entry.pack(pady=10)

calc_button =Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=5)

result_label =Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()