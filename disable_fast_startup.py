import subprocess

def run_as_admin(cmd):
    """
    Run a command as an administrator.
    """
    try:
        # Construct the command
        command = f'powershell -Command "Start-Process cmd.exe -ArgumentList \'/c {cmd}\' -Verb RunAs"'
        
        # Execute the command
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        return result.stdout.decode(), result.stderr.decode()
    except subprocess.CalledProcessError as e:
        return e.stdout.decode(), e.stderr.decode()

def disable_fast_startup():
    """
    Disable the Fast Startup feature in Windows.
    """
    # Command to disable Fast Startup
    command = "powercfg -h off"
    
    # Run the command as an administrator
    stdout, stderr = run_as_admin(command)
    
    if stderr:
        print(f"Error: {stderr}")
    else:
        print(f"Success: {stdout}")

if __name__ == "__main__":
    disable_fast_startup()
