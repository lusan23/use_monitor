from pystray import MenuItem as item, Icon

from PIL import Image
from subprocess import Popen
from os import getppid, kill
import signal 
from app_gui import start as gui_start
from multiprocessing import freeze_support, Process 
gui_process = None
def open_gui():
    global gui_process
    
    gui_process = Process(target=gui_start)
    gui_process.start()

def end_session(icon, item):
    global gui_process
    try:
        if (gui_process):
            print("terminating gui...")
            gui_process.terminate()

        ppid = getppid()
        kill(ppid, signal.SIGTERM)
        icon.stop()
    except OSError as e:
        print(f"Failed to send SIGTERM to parent process {getppid()}: {e}")
      

def default_action(icon, item):
    print("default")

def start_icon():
    image = Image.open("icon.png")

    menu = (
        item('Use Monitor', open_gui, default=True, visible=True),
        item('Quit', end_session)
    )

    icon = Icon("UM", image, "Use Monitor", menu)
    icon.run()

    background_procress = Popen(["python", "background_process.py"], shell=False)

#start_icon()