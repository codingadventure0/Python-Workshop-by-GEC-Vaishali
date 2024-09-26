from tkinter import *

root = Tk()
root.title("EVM")
root.geometry("500x500")

def save_file():
    file=filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file is not None:
        file.write(text_area.get(1.0, END))
        file.close()

text_area=Text(root, wrap="word")
text_area.pack(expand=1, file="both")

save_button=Button(root, text="Save", command=save_file)
save_button.pack(pady=10)

root.mainloop()