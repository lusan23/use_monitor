from subprocess import Popen

if __name__ == "__main__":    
    Popen(["python", "background_process.py"], shell=True)
    Popen(["python", "stray_sys.py"])
    