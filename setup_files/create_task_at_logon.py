import win32com.client
import os

TASK_TRIGGER_LOGON = 9
TASK_ACTION_EXEC = 0
TASK_ACTION_CREATE_OR_UPDATE = 4
TASK_LOGON_INTERACTIVE_TOKEN = 3
# connect to task scheduler
scheduler = win32com.client.Dispatch("Schedule.Service")
scheduler.Connect()

# create new task
task_ref = scheduler.NewTask(0)

# CREATE ACTION
action = task_ref.Actions.Create(TASK_ACTION_EXEC)
action.ID = "TRIGGER RECORD SESSION"
action.Path = f"{os.getcwd()}\\call_main.bat"

# Set Settings
task_ref.RegistrationInfo.Description = "Use Monitor shutdown script"
task_ref.Settings.Enabled = True
task_ref.Settings.StopIfGoingOnBatteries = False
settings = task_ref.Settings

# Create Trigger

trigger = task_ref.Triggers.Create(TASK_TRIGGER_LOGON)
trigger.Id = "LogonTriggerId"
trigger.UserId = os.environ.get("USERNAME")

# Set registration Info
info = task_ref.RegistrationInfo
info.Author = "Use Monitor"
info.Description = "Execute a script that saves the current session time plus additional info"
settings = task_ref.RegistrationInfo

# Register the task
root_folder = scheduler.GetFolder("\\")
result = root_folder.RegisterTaskDefinition("Time Monitor Startup Script", 
                                          task_ref, TASK_ACTION_EXEC, "", "",
                                          TASK_LOGON_INTERACTIVE_TOKEN)