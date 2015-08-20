import Tkinter as tk
import urllib2
def get_server_ip():
    pass
def get_server_port():
    pass

def on_key_press(event):
    server_ip = get_server_ip()
    server_port = get_server_port()
    urllib2.urlopen("{0}:{1}".format(server_ip, server_port))

root = tk.Tk()
root.bind('<KeyPress>', on_key_press)
root.mainloop()
