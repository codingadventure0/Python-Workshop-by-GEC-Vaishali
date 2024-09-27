from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("NotePad")
root.geometry("500x700")

def save_file():
    file=filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file is not None:
        file.write(text_area.get(1.0, END))
        file.close()

text_area=Text(root, wrap="word")
text_area.pack(expand=1, fill="both")

save_button=Button(root, text="Save", command=save_file)
save_button.pack(pady=10)

root.mainloop()