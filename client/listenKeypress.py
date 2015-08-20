import Tkinter as tk

def onKeyPress(event):
    print "hello world"

root = tk.Tk()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
