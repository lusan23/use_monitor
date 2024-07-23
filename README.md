# Use Monitor ⏱️
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
1. **Tracking Time:**
   Once you log on, you should see a terminal screen. This script will keep track of your time when you shut down your PC.

   ![Terminal Screen](image-1.png)

2. **Viewing Time Spent:**
   Run the following command to see your time spent:
   ```
   python app_gui.py
   ```
   ![GUI Screen](image.png)
