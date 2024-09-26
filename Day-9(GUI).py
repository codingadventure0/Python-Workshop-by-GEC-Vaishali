from tkinter import *

root = Tk()
root.title("EVM")
root.geometry("500x500")

"""
text = Text(root, height=10, width=50)
text.grid(row=0, column=0)

def welcome_msg():
    text.insert(END, "Welcome to Python Workshop.")  

btn = Button(root, text="Welcome", command=welcome_msg)
btn.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
"""
v1=0
v2=0
def vote1():
    global v1
    v1=v1+1
    print("Value of v1:",v1)

def vote2():
    global v2
    v2=v2+1
    print("Value of v2:",v2)

def result():
    if v1>v2:
        Label(root,text="Winner: Party-1",height=5,width=20).grid(row=3,column=4)
    elif v1==v2:
        Label(root,text="Result Pending: Due to equal votes.",height=5,width=20).grid(row=3,column=4)
    else:
        Label(root,text="Winner: Party-2",height=5,width=20).grid(row=3,column=4)
    btn1.config(state="disabled")
    btn2.config(state="disabled")

Label(root,text="Party-1",height=2,width=10).grid(row=1,column=1)
btn1=Button(root,text="Vote", command=vote1)
btn1.grid(row=1,column=2)

Label(root,text="Party-2",height=2,width=10).grid(row=2,column=1)
btn2=Button(root,text="Vote", command=vote2)
btn2.grid(row=2,column=2)

btn3=Button(root,text="Result", command=result)
btn3.grid(row=3,column=3)

#w=Entry(root, text="Enter your text here....")
#w.grid(row=6, column=1)
