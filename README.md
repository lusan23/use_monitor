## How to set it up

### Fast Startup must be unable
#### It allows the boot time to be registered once you shut down
``python setup_files\disable_fast_startup.py ``

### Create Trigger task
``python setup_files\create_task_at_logon.py`` <br />
it creates a task at the windows task scheduler to trigger the `back_ground_process.py` file, which does the time storage. 

### Allow script to be executed at shutdown
#### Configure Shutdown options to allow top-level scripts to hold shutdown event
``python setup_files\config_execute_at_shutdown_perm.py``

## python required packages:
PyQt6 (GUI lib) <br />
``pip install pyqt6==6.7.0`` <br />
psutil (only used for once, so the execute at shutdown script can work.) <br />
``pip install psutil==5.9.8`` <br />
pywin32 (For the time spent estimation )<br />
``pip install pywin32==306``
pystray (For the module that creates the Hiden Icon on Windows's taskbar)
``pip install pystray==0.19.5``
<br/>
after installing everything restart your Machine

## Getting started
Once you log on you must see a terminal screen, that's the script that will keep track of your time once you shut down your pc.<br />
![alt text](image-1.png)__
<br />
By running ``python app_gui.py`` you'll see your time spent. <br />
![alt text](image.png)
<br />

