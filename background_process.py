import win32api 
import win32con
import win32gui
import time_session_utility as rts
import datetime
from time_history import start, update_sessions_history

rts_called = False

def wnd_proc(hwnd, msg, wparam, lparam):
    message_map = [win32con.WM_QUERYENDSESSION, win32con.WM_ENDSESSION]

    # Get current date and time
    current_datetime = datetime.datetime.now()

    # Format date and time as string
    datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Windows message: {str(msg)}, {datetime_str}")
    print(f"rts_called:{rts_called}")
 

    if msg in message_map or msg == 799:
        # Handle the shutdown request here
        try:
            start()
        except Exception as e:
            with open("./shutdown_log.txt", "a") as f:
                f.write(str(e))
        return True  # Return True to allow shutdown, False to deny it
    
    return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

def create_window():

    wc = win32gui.WNDCLASS()
    wc.lpfnWndProc = wnd_proc
    wc.lpszClassName = "ShutdownHandleFunc"
    wc.hInstance = win32api.GetModuleHandle(None)
    class_atom = win32gui.RegisterClass(wc)
    hwnd = win32gui.CreateWindow(class_atom, "ShutdownHandlerWindow", 
                                 0, 0, 0, 0, 0, 0, 0, wc.hInstance, None)
    return hwnd

def main():
    hwnd = create_window()
    print(f"Window created with hwnd: {hwnd}") 
    win32gui.PumpMessages()

if __name__ == "__main__":
    update_sessions_history()
    print("-"*20)
    main()
  
