@echo off
setlocal

rem Set the path to the file you want to create a shortcut for
set current_path=%CD%
set "file_path=%current_path%\background_process.py"

rem Get the path to the Startup folder
set "startup_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

rem Define the shortcut name and path
set "shortcut_name=use_monitor"
set "shortcut_path=%startup_folder%\%shortcut_name%.lnk"
cd
rem Create the shortcut using PowerShell
powershell -Command "$WScriptShell = New-Object -ComObject WScript.Shell; $Shortcut = $WScriptShell.CreateShortcut('%shortcut_path%'); $Shortcut.TargetPath = '%file_path%'; $Shortcut.Save()"

echo Shortcut created at %shortcut_path%
pause
