from ctypes import windll
import os

class AdminRightsRequirer:
    def _init__(self):
        pass
    def is_admin(self):
        try:
            return windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def __run_as_admin(self, function_to_exec):
        if self.is_admin():
            result = function_to_exec()
            return result
        else:
            # Re-run the script with admin rights
            windll.shell32.ShellExecuteW(None, "runas", os.sys.executable,
                                          __file__, None, 1)
