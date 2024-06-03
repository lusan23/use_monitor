from datetime import datetime
import json
import os

def get_time_date():
    output_dict = {}
    
    # get the current date and time 
    now = datetime.now()

    # breakdown the time and date
    hour,minute,second = int(now.strftime("%H")), int(now.strftime("%M")), float(now.strftime("%S"))
    day,month,year = int(now.strftime("%d")), int(now.strftime("%m")), int(now.strftime("%Y"))
    
    # format it as a dict
    output_dict["hour"] = hour 
    output_dict["min"] = minute 
    output_dict["sec"] = second 
    
    output_dict["day"] = day
    output_dict["month"] = month
    output_dict["year"] = year

    return [output_dict]
    
    
def save_info(dict):    
    # save it as a file

    # verify if there's a file already
    if os.path.exists('time_spent_today_data.json'):
        with open("time_spent_today_data.json", "r") as file:
            existent_data = json.load(file)
            existent_data.append(dict)
        
        with open("time_spent_today_data.json", "w") as file:
            json.dump(existent_data, file, indent=4)



    else:
        print('File does not exist')
        with open("time_spent_today_data.json", "w") as file:
            json.dump(dict, file, indent=4)
        
def is_shutdown(times_list):
    with open("time_spent_today_data.json", "r") as file:
        existent_data = json.load(file)
        if len(existent_data) == 2:
            return True
        else:
            return False
        
def calc_time_spent():
    with open("time_spent_today_data.json", "r") as file:
        existent_data = json.load(file)
        if (is_shutdown(existent_data)):
              pass              
        else:
            pass
def start():
    now_data = get_time_date()
    save_info(now_data)


start()