from datetime import datetime, timedelta
from json import load, dump
from psutil import boot_time as ps_boot_time
from re import sub, match

def calc_time_spent() -> timedelta:
    # calculate the time up and return it

    # Get the boot time in seconds since the epoch
    boot_time_timestamp = ps_boot_time()

    # Convert it to a datetime object
    boot_time = datetime.fromtimestamp(boot_time_timestamp)

    # Get the current time
    current_time = datetime.now()

    # Calculate the difference
    uptime = current_time - boot_time

    return uptime

def get_session_boot_time():
    current_but_time =  ps_boot_time()
    dt_boot_time = datetime.fromtimestamp(current_but_time)
    dt_boot_time = dt_boot_time.replace(second=0, microsecond=0)
    return dt_boot_time


def load_dict_hist(history_key="today_sessions", 
                   load_whole_dict=False):
    '''
    Load the list of sessions 
    '''
    directory_path="time_sessions_history"
    filename="time_spent_session_history.json"
    file_path = f"{directory_path}/{filename}"

    with open(file_path, "r") as file:
        dict_hist = load(file)
        if load_whole_dict:
            return dict_hist
        return dict_hist[history_key]

def write_dict_hist(updated_dict_hist: {list}):
    '''
    write the list of sessions 
    '''
    directory_path="time_sessions_history"
    filename="time_spent_session_history.json"
    file_path = f"{directory_path}/{filename}"

    with open(file_path, "w") as file:
        dump(updated_dict_hist, file, indent=8)


def get_time_boot_or_timespent(session_info: str, get_tb=True) -> str:
    '''
    
    From the raw string that contains a session info extracts the time boot or timespent plus record date/time 
    
    Parameters:

    @session_info - the session's string

    @get_tb: 
        True - return the boot time of the given session
        False - return the session info
        
    '''
    session_info = session_info.split("BOOT_TIME:")
    if get_tb:
        
        return session_info[1]
    else:
        
        return session_info[0][:len(session_info[0]) - 2]


def get_record_time(session_info: str):
    tmp = session_info.split(",")
    tmp_comma_splited = tmp[2]
    tmp_space_splited = tmp_comma_splited.split(" ")
    return tmp_space_splited[2]

def string_to_timedelta(value) -> timedelta:  
    """
    Convert a string into a timedelta object.
    """
    splited = value.split(":")
    splited = [item.split(",") for item in splited]
    splited = [elem for sublist in splited for elem in sublist]


    splited = splited[:4] 
    args_dict = {}
    # print(splited)

    if len(splited) == 4:
        args_dict["days"] =  int(splited[0][0])
    else:
        args_dict["days"] = 0

    args_dict["hours"] =  int(splited[1])
    args_dict["minutes"] =  int(splited[2])
    args_dict["seconds"] =  int(splited[3])
    
    return timedelta(**args_dict)

def remove_letters(string):
    return sub(r"[a-z]", "", string)

def time_spent_to_string(up_time, include_date=False, ):
    # handles any format of spent to the default days, hour?min?sec

    # handle if there is days, hours, min and sec
    
    splited = str(up_time).split(":")
    splited_len = len(splited)
    splited = [item.split(",") for item in splited]
    splited = [elem for sublist in splited for elem in sublist]
    splited = [elem.replace(" day", "") for elem in splited]
    splited = [remove_letters(elem) if bool(match(r"\d[a-z]", elem)) else elem for elem in splited]
    splited = [int(float(elem)) for elem in splited]
    
    if include_date:
        current_time = datetime.now()
        current_time_str = f"{current_time.year}-{current_time.month}-{current_time.day} {current_time.strftime("%H:%M:%S")}"
        splited.append(current_time_str)
        
        while len(splited) < 5: 
            splited.insert(0,0)
        result = "{} day, {}:{}:{}, {}".format(*splited)
        return result    
    
    while len(splited) < 4: 

        splited.insert(0,0)

    return "{} day, {}:{}:{}".format(*splited)    

