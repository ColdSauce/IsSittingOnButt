import Tkinter as tk

def onKeyPress(event):
    text.insert('end', 'You pressed %s\n' % (event.char, ))

root = tk.Tk()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
