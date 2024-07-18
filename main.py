from multiprocessing import Process, freeze_support
from os import getpid,system
from signal import signal, SIGTERM
from background_process import start as bg_start
from stray_sys import start_icon

processes = []

def signal_handler(a, b):
    global processes
    for procs in processes:
        procs.terminate()
    system("kill", getpid())

def main_process():
    global processes
    freeze_support()
    p = Process(target=bg_start,)
    processes.append(p)
    p.start()
    icon_process = Process(target=start_icon, 
                                    )
    processes.append(icon_process)  
    icon_process.start()

    signal(SIGTERM, signal_handler)
    

    
if __name__ == "__main__":
    
    main_process()