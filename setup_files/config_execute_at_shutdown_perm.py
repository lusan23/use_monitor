""" Change a configuration at Group Policy Editor unabling windows of force terminate the script on the shutdown event"""
import winreg as reg
import os
import ctypes
import common

class PolicyCreater(common.AdminRightsRequirer):
    def __init__(self) -> None:
        super().__init__()
        # Path to the registry key
        self.key_path = r"Software\\Policies\\Microsoft\\Windows\\System"
        # Open the key (creates it if it doesn't exist)  
        self.key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, self.key_path)

    def __run_as_admin(self, functions_to_exec: list):
        """
        On this change, run as admin takes many functions
        """
        if self.is_admin():
            for function in functions_to_exec:
                print(f"function{function.__name__} executed!!!")
                function() 
        else:
            # Re-run the script with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", os.sys.executable,
                                          __file__, None, 1)
    def enable_policy(self):
        try:
            # Set the value (0 to disable, 1 to enable)
            self.__run_as_admin([reg.SetValueEx(self.key, "DisableForceShutdown", 
                                             0, reg.REG_DWORD, 1),
                                             # Close the key
                                             reg.CloseKey(self.key)])
            
        
            
            print("Policy has been enabled successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")



    