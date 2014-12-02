import Tkinter
import tkMessageBox

top = Tkinter.Tk()
# Code to add widgets will go here...
def helloCallBack():
    tkMessageBox.showinfo("My window", "Hello world")
w = Tkinter.Button(top, text="Hello", command=helloCallBack)
w.pack()
top.mainloop()
