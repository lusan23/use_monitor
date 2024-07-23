# Use Monitor ⏱️

## Introduction
The main purpose of this project was to get me on track with my learning journey after a couple of months without coding at all, 
so if by looking at it you'd like to point out where I could improve, please let me know!

## Index
1. [How to Set It Up](#how-to-set-it-up)
   1. [Disable Fast Startup](#1-disable-fast-startup)
   2. [Create Trigger Task](#2-create-trigger-task)
   3. [Allow Script Execution at Shutdown](#3-allow-script-execution-at-shutdown)
2. [Required Python Packages](#required-python-packages)
3. [Getting Started](#getting-started)
   1. [Tracking Time](#1-tracking-time)
   2. [Viewing Time Spent](#2-viewing-time-spent)
4. [Binary Version](#binary-version)
5. [Issues](#issues)

## How to Set It Up

### 1. Disable Fast Startup
Fast Startup needs to be disabled to ensure boot time is registered when you shut down.
Run the following command:
```
python setup_files/disable_fast_startup.py
```

### 2. Create Trigger Task
This task will be created in the Windows Task Scheduler to trigger the `back_ground_process.py` file, which records the time spent.
Run the following command:
```
python setup_files/create_task_at_logon.py
```

### 3. Allow Script Execution at Shutdown
Configure the shutdown options to allow top-level scripts to hold the shutdown event.
Run the following command:
```
python setup_files/config_execute_at_shutdown_perm.py
```

## Required Python Packages
Install the following packages using `pip`:

1. **PyQt6** (GUI library)
   ```
   pip install pyqt6==6.7.0
   ```

2. **psutil** (used for shutdown script)
   ```
   pip install psutil==5.9.8
   ```

3. **pywin32** (for time estimation)
   ```
   pip install pywin32==306
   ```

4. **pystray** (for creating the hidden icon in the Windows taskbar)
   ```
   pip install pystray==0.19.5
   ```

After installing all the packages, restart your machine.

## Getting Started
### 1. Tracking Time
Once you log on, you should see a terminal screen. This script will keep track of your time when you shut down your PC.

![Terminal Screen](image-1.png)

### 2. Viewing Time Spent
Run the following command to see your time spent:
```
python app_gui.py
```
![GUI Screen](image.png)

## Binary Version

As the project was compiled using pyinstaller you won't need a Python interpreter to use it, all the dependencies are included in `_internal_`.
The setup_files folder was also compiled as `setup_main.exe`.

### How to Install

You may download it from the releases and extract and place the folder anywhere you want,  it's needed to execute `setup_main.exe` as it will allow Use Monitor to do its saving sessions, calculate 
the time spent through the boot time, and create the task which will execute `main.exe` at log on.

## Issues
When Use Monitor is closed, it is supposed to also end all of the other processes, but two processes keep running even after the end function.
I'm trying to figure out why this is happening. If you'd like to help, here's my Discord: #luan98982
