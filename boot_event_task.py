from datetime import datetime
import json
import os

def str2time(string_):
    return datetime.strptime(string_, "%H:%M:%S")

def get_time_date():
    output_dict = {}
    
    # get the current date and time 
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    # breakdown the time and date
    #hour,minute,second = int(now.strftime("%H")), int(now.strftime("%M")), float(now.strftime("%S"))
    day,month,year = int(now.strftime("%d")), int(now.strftime("%m")), int(now.strftime("%Y"))
    
    # format it as a dict
    '''
    output_dict["hour"] = hour 
    output_dict["min"] = minute 
    output_dict["sec"] = second 
    '''
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
            time_object = [str2time(existent_data[0]["time"]), 
                           str2time(existent_data[1]["time"])]
            
            print(f"RESULTADO:{time_object[1] - time_object[0]}")          
        else:
            pass
def clean_data():
    file_path = "time_spent_today_data.json"
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    
def start():
    now_data = get_time_date()
    save_info(now_data)
    calc_time_spent()
    clean_data()


start()