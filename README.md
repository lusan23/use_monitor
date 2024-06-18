## Requirements
Fast Startup must be unable
``python disable_fast_startup.py ``
Configure Shutdown options to allow top level apps hold shutdown event
``python config_execute_at_shutdown_perm.py``
Configure startup 
``.\config_startup.bat``

## python required packages:
PyQt6
psutil (only used for once, so the execute at shutdown script can work.)
pywin32