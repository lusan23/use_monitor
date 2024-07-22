import win32com.client
import os
import common
from win32api import FormatMessage

class TaskCreater(common.AdminRightsRequirer):
    def __init__(self) -> None:
        super().__init__() 
        self.TASK_TRIGGER_LOGON = 9
        self.TASK_ACTION_EXEC = 0
        self.TASK_ACTION_CREATE_OR_UPDATE = 4
        self.TASK_LOGON_INTERACTIVE_TOKEN = 3

    def __create_new_task(self):
        # connect to task scheduler
        self.scheduler = win32com.client.Dispatch("Schedule.Service")
        self.scheduler.Connect()

        # create new task
        self.task_ref = self.scheduler.NewTask(0)

    def __create_action(self):
        # CREATE ACTION
        self.action = self.task_ref.Actions.Create(self.TASK_ACTION_EXEC)
        self.action.ID = "TRIGGER RECORD SESSION"
        self.action.Path = f"{os.getcwd()}..\\call_main.bat"

    def __set_settings(self):
        # Set Settings
        self.task_ref.RegistrationInfo.Description = "Use Monitor shutdown script"
        self.task_ref.Settings.Enabled = True
        self.task_ref.Settings.StopIfGoingOnBatteries = False
        self.settings = self.task_ref.Settings

    def __run_as_admin(self, function_to_exec):
        return super().__run_as_admin(function_to_exec)
    def __set_trigger(self):
        # Create Trigger

        self.trigger = self.task_ref.Triggers.Create(self.TASK_TRIGGER_LOGON)
        self.trigger.Id = "LogonTriggerId"
        self.trigger.UserId = os.environ.get("USERNAME")

    def register_task(self, author, descrip):
        self.__create_new_task()
        self.__create_action()
        self.__set_settings()
        self.__set_trigger()
            
        # Set registration Info
        info = self.task_ref.RegistrationInfo
        info.Author = author
        info.Description = descrip
        self.settings = self.task_ref.RegistrationInfo

        # Register the task
        self.__root_folder = self.scheduler.GetFolder("\\")
        
        result = self.__run_as_admin(self.__root_folder.RegisterTaskDefinition(author, 
                                                self.task_ref, self.TASK_ACTION_EXEC, "", "",
                                                self.TASK_LOGON_INTERACTIVE_TOKEN)) 
        return result
    