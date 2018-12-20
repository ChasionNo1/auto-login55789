from tkinter import *


def clicked():
    a = var1.get()
    b = var2.get()
    text1.insert(INSERT, a+b)
    text1.pack()


top = Tk()
top.title('dijkstra算法')
top.geometry('400x400')
btn = Button(command=clicked)
text1 = Text(width=100, height=20, fg='red')
var1 = StringVar()
var2 = StringVar()
entry1 = Entry(textvariable=var1).pack(side=TOP, ipadx=2, ipady=5)
entry2 = Entry(textvariable=var2).pack(side=TOP, ipadx=2, ipady=5)
btn['text'] = '启动'
btn.pack(ipadx=20, ipady=10, side="bottom")
top.mainloop()
