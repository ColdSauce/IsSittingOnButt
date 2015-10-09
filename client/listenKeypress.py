import Tkinter as tk
import yaml
import requests
import tty, termios, sys
import thread
import time

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

def on_key_press():
    server_ip = get_server_ip()
    server_port = get_server_port()
    url_to_request = "http://{0}:{1}/pressed".format(server_ip, server_port)
    requests.get(url_to_request)

def on_key_released():
    server_ip = get_server_ip()
    server_port = get_server_port()
    url_to_request = "http://{0}:{1}/released".format(server_ip, server_port)
    requests.get(url_to_request)

def getchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

is_pressed = False

def get_char_thread():
    global is_pressed
    while 1:
        ch = getchar()
        is_pressed = True

def check_is_pressed(delay):
    global is_pressed
    while 1:
        time.sleep(delay)
        if is_pressed:
            on_key_press()
            is_pressed = False
        else:
            on_key_released()

thread.start_new_thread(get_char_thread, ())
thread.start_new_thread(check_is_pressed, (5,))
while 1:
    pass
