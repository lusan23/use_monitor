""" Change a configuration at Group Policy Editor unabling windows of force terminate the script on the shutdown event"""
import winreg as reg
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def enable_policy():
    try:
        # Path to the registry key
        key_path = r"Software\\Policies\\Microsoft\\Windows\\System"
        
        # Open the key (creates it if it doesn't exist)
        key = reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path)
        
        # Set the value (0 to disable, 1 to enable)
        reg.SetValueEx(key, "DisableForceShutdown", 0, reg.REG_DWORD, 1)
        
        # Close the key
        reg.CloseKey(key)
        
        print("Policy has been enabled successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if is_admin():
        enable_policy()
    else:
        # Re-run the script with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", os.sys.executable, __file__, None, 1)