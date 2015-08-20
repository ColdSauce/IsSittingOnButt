import Tkinter as tk
import yaml
import requests


yaml_contents = None

def get_yaml_contents():
    global yaml_contents
    if yaml_contents is None:
        with open("config/config.yml", "r") as f:
            yaml_contents = yaml.load(f)
    return yaml_contents

def get_server_ip():
    yaml_contents = get_yaml_contents()
    return yaml_contents["SERVER_IP"]

def get_server_port():
    yaml_contents = get_yaml_contents()
    return yaml_contents["SERVER_PORT"]

def on_key_press(event):
    server_ip = get_server_ip()
    server_port = get_server_port()
    url_to_request = "http://{0}:{1}/pressed".format(server_ip, server_port)
    requests.get(url_to_request)

def on_key_released(event):
    server_ip = get_server_ip()
    server_port = get_server_port()
    url_to_request = "http://{0}:{1}/pressed".format(server_ip, server_port)
    requests.get(url_to_request)

root = tk.Tk()
root.bind('<KeyPress>', on_key_press)
root.bind('<KeyRelease>', on_key_released)
root.mainloop()
