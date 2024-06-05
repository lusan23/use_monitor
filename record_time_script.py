from datetime import datetime,timedelta
import re
import json
import os

def str2time(string_):
    return datetime.strptime(string_, "%H:%M:%S")

def get_time_date():
    output_dict = {}
    
    # get the current date and time 
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    # breakdown the  date
    day,month,year = int(now.strftime("%d")), int(now.strftime("%m")), int(now.strftime("%Y"))
    # format it as a dict
    output_dict["time"] = time
    output_dict["day"] = day
    output_dict["month"] = month
    output_dict["year"] = year

    return output_dict
    
    
def save_info(dict):    
    # save it as a file

    # verify if there's a file already
    if os.path.exists('time_spent_today_data.json'):
        with open("time_spent_today_data.json", "r") as file:
            existent_data = json.load(file)
            if (len(existent_data) < 2):
                existent_data.append(dict)
        
        with open("time_spent_today_data.json", "w") as file:
            json.dump(existent_data, file, indent=4)

    else:
        print('File does not exist')
        with open("time_spent_today_data.json", "w") as file:
            json.dump([dict], file, indent=4)
        
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
        
def calc_time_spent() -> str:
    # calculate the time and return it
    
    with open("time_spent_today_data.json", "r") as file:
        existent_data = json.load(file)
        if (is_shutdown()):
            time_object = [str2time(existent_data[0]["time"]), 
                        str2time(existent_data[1]["time"])]
            
            return str(time_object[1] - time_object[0])

        else:
            return "00:00:00"
        
def clean_data() -> None:
    file_path = "time_spent_today_data.json"
    if (is_shutdown()):    
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")

def string_to_timedelta(value):
    """
    Convert a string representation of a duration to a timedelta object.
    """
    hour = int(value[:2])
    min = int(value[3:4])
    sec = int(value[6:])
    return timedelta( hours=hour, minutes=min, seconds=sec,)

def add_left_zero(string):
    print(string[:2])
    if ":" in string[:2]:
        return  "0" + string
    return string

def save_acmltd_time(time_spent):
    # update the current total time spent

    if os.path.exists('total_time_spent.json'):
        print("shutdown event")

        with open("total_time_spent.json", "r") as file:
            crt_total_str = json.load(file)
            current_total = string_to_timedelta(crt_total_str) 
            time_spent = add_left_zero(time_spent)
            current_total += string_to_timedelta(time_spent)
        
        with open("total_time_spent.json", "w") as file:
            str_time_total = str(current_total)
            # make sure that hour find has left zero

            str_time_total = add_left_zero(str_time_total)

            json.dump(str_time_total, file, indent=4)
        
    else:
        print("boot event")
        with open("total_time_spent.json", "w") as file:
            json.dump("00:00:00", file)
    

def start():
    now_data = get_time_date()
    save_info(now_data)

    
    time_spent = calc_time_spent()
    save_acmltd_time(time_spent)
    clean_data()
    


start()