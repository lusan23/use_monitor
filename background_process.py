import win32api 
import win32con
import win32gui
import record_time_script as rts


def wnd_proc(hwnd, msg, wparam, lparam):
    print("windows message:"+str(msg))
    if msg == 800:
    #if msg == win32con.WM_QUERYENDSESSION:
        # HANDLE THE SHUTDOWN REQUEST HERE
        rts.start()
        return True # return true to allow shutdown, false to deny it
    elif msg == win32con.WM_ENDSESSION:
        # Clean up if needed
        if wparam: #wparam is true if session is ending
            print("WM_ENDSESSION received, session ending")
        else:
            print("WM_ENDSESSION received, session not ending")

    return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

def create_window():
    wc = win32gui.WNDCLASS()
    wc.lpfnWndProc = wnd_proc
    wc.lpszClassName = "ShutdownHandleFunc"
    wc.hInstance = win32api.GetModuleHandle(None)
    class_atom = win32gui.RegisterClass(wc)
    hwnd = win32gui.CreateWindow(class_atom, "ShutdownHandlerWindow", 0, 0, 0, 0, 0, 0, 0, wc.hInstance, None)
    return hwnd
'''
while True:
    print("Waiting for shutdown event...")
    sleep(1)
'''
def main():
    hwnd = create_window()
    print(f"window created with hwnd: {hwnd}") 
    win32gui.PumpMessages()

if __name__ == "__main__":
    main()