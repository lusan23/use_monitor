from datetime import datetime,timedelta
import json
import os
import datetime 
import psutil

def str2time(string_):
    return datetime.strptime(string_, "%H:%M:%S")

def is_shutdown() -> bool:
    '''
    Verify if it`s second time the script is executed 
    '''
    with open("time_spent_today_data.json", "r") as file:
        existent_data = json.load(file)
        if len(existent_data) == 2:
            return True
        else:
            return False
        
def calc_time_spent() -> timedelta:
    # calculate the time up and return it

    # Get the boot time in seconds since the epoch
    boot_time_timestamp = psutil.boot_time()

    # Convert it to a datetime object
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)

    # Get the current time
    current_time = datetime.datetime.now()

    # Calculate the difference
    uptime = current_time - boot_time

    return uptime
        
def string_to_timedelta(value):
    """
    Convert a string representation of a duration to a timedelta object.
    """
    splited = value.split(":")
    args_dict = {}

    if len(splited) == 4:
        args_dict["days"] =  int(splited[0])
    
    args_dict["days"] = 0
    args_dict["hours"] =  int(splited[1])
    args_dict["minutes"] =  int(splited[2])
    args_dict["seconds"] =  float(splited[3])
    

    
    return datetime.timedelta(**args_dict)

def add_left_zero(string):
    print(string[:2])
    if ":" in string[:2]:
        return  "0" + string
    return string

def save_acmltd_time(time_spent):
    # update the current total time spent

    if os.path.exists('total_time_spent.json'):

        with open("total_time_spent.json", "r") as file:
            crt_total_str = json.load(file)
            current_total = string_to_timedelta(crt_total_str) 
            current_total += time_spent
        
        with open("total_time_spent.json", "w") as file:
            str_time_total = str(current_total)
            # make sure that hour find has left zero
            str_time_total = add_left_zero(str_time_total)

            json.dump(str_time_total, file, indent=4)

    else:
        print("boot event")
        with open("total_time_spent.json", "w") as file:
            str_time_spent = str(time_spent)
            json.dump("0:" + str_time_spent, file)
    

def start():
    time_spent = calc_time_spent()
    save_acmltd_time(time_spent)

start()