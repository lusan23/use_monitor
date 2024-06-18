from datetime import datetime, timedelta
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
        
def get_current_time() -> datetime:
    """
    Get the current time and convert it to string

    """

def string_to_timedelta(value) -> timedelta:  
    """
    Convert a string into a timedelta object.
    """
    splited = value.split(":")
    splited = [item.split(",") for item in splited]
    splited = [elem for sublist in splited for elem in sublist]


    splited = splited[:4] 
    args_dict = {}
    print(splited)

    if len(splited) == 4:
        args_dict["days"] =  int(splited[0][0])
    else:
        args_dict["days"] = 0

    args_dict["hours"] =  int(splited[1])
    args_dict["minutes"] =  int(splited[2])
    args_dict["seconds"] =  int(splited[3])
    
    return datetime.timedelta(**args_dict)

def time_spent_to_string(up_time, include_date=False, ):
    # handles any format of spent to the default days, hour?min?sec

    # handle if there is days, hours, min and sec
    
    splited = str(up_time).split(":")
    splited_len = len(splited)
    splited = [item.split(",") for item in splited]
    splited = [elem for sublist in splited for elem in sublist]
    splited = [elem.replace(" day", "") for elem in splited]
    
    splited = [int(float(elem)) for elem in splited]
    if include_date:
        current_time = datetime.datetime.now()
        current_time_str = f"{current_time.year}-{current_time.month}-{current_time.day} {current_time.strftime("%H:%M:%S")}"
        splited.append(current_time_str)
        
        while len(splited) < 5: 
            splited.insert(0,0)
        result = "{} day, {}:{}:{}, {}".format(*splited)
        return result    
    
    while len(splited) < 4: 

        splited.insert(0,0)

    return "{} day, {}:{}:{}".format(*splited)    
    

def add_left_zero(string) -> str:
    print(string[:2])
    if ":" in string[:2]:
        return  "0" + string
    return string

def save_acmltd_time(time_spent) -> None:
    # update the current total time spent
    # make sure that the file is created on the  script folder, not the shortcut
    current_dir = os.path.dirname(os.path.realpath(__file__))
    json_file_path = os.path.join(current_dir, 'total_time_spent.json')

    if os.path.exists(json_file_path):

        with open(json_file_path, "r") as file:
            crt_total_str = json.load(file)
            if crt_total_str == None:
                raise Exception("File empty!!!")
            current_total = string_to_timedelta(crt_total_str) 
            time_spent_str = string_to_timedelta(time_spent)
            current_total += time_spent_str
        
        with open(json_file_path, "w") as file:
            str_time_total = time_spent_to_string(current_total, include_date=True)

            json.dump(str_time_total, file, indent=4)

    else:
        print("boot event")
        with open(json_file_path, "w") as file:
            str_time_spent = time_spent_to_string(time_spent, include_date=True)
            json.dump(str_time_spent, file)
    
def load_total_time() -> str:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    json_file_path = os.path.join(current_dir, 'total_time_spent.json')
    try:
        if os.path.exists(json_file_path):

            with open(json_file_path, "r") as file:
                crt_total_str = json.load(file)
                
                return crt_total_str
    except Exception as e:
        print(e)
            

def start():
    time_spent = calc_time_spent()

    try:

        save_acmltd_time(time_spent_to_string(time_spent))
    
    except Exception as e:

        folder_name = "logs"
        # Get current date and time
        current_datetime = datetime.datetime.now()

        # Format date and time as string
        datetime_str = current_datetime.strftime("%Y-%m-%d")
        file_name=datetime_str + ".txt"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

            # Create or open the text file in write mode
            file_path = os.path.join(folder_name, file_name)

            with open(file_path, 'w') as file:
                file.write(e)

