from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('500x400')
lbl1 = Label(root, text="Enter a Number")
lbl1.grid(column=0, row=0)
txt1 = Entry(root, width=10)
txt1.grid(column=1, row=0)

lbl2 = Label(root, text="Operation")
lbl2.grid(column=0, row=1)
txt2 = Entry(root, width=10)
txt2.grid(column=1, row=1)

lbl3 = Label(root, text="Enter a Number")
lbl3.grid(column=0, row=2)
txt3 = Entry(root, width=10)
txt3.grid(column=1, row=2)

lbl4 = Label(root, text="")
lbl4.grid(column=1, row=4)


def clicked():
    num1 = int(txt1.get())
    opr = txt2.get()
    num2 = int(txt3.get())
    res = 0
    invalid = False
    if (opr == '+'):
        res = num1 + num2
    elif (opr == '-'):
        res = num1 - num2
    else:
        invalid = True

    if (invalid):
        res = 'invalid operator'
    lbl4.configure(text=res)
    txt1.delete(0, END)
    txt2.delete(0, END)
    txt3.delete(0, END)


btn = Button(root, text="Calculate",
             fg="red", command=clicked)
btn.grid(column=1, row=3)
root.mainloop()

