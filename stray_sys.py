from pystray import MenuItem as item
import pystray
from PIL import Image
from subprocess import run, Popen
from os import getppid, kill
from signal import SIGTERM
from psutil import Process

def open_gui():
    Popen(["python", "app_gui.py"], shell=True)

def end_session(icon, item):
    try:
        prnt_id = getppid()
        prnt_prcss = Process(prnt_id)
        prnt_prcss.terminate()
        icon.stop()
    except OSError as e:
        print(f"Failed to send SIGTERM to parent process {getppid()}: {e}")
        exit()

def default_action(icon, item):
    print("default")

def start_icon():
    image = Image.open("icon.png")

    menu = (
        item('Use Monitor', open_gui, default=True, visible=True),
        item('Quit', end_session)
    )

    icon = pystray.Icon("UM", image, "Use Monitor", menu)
    icon.run()

start_icon()