from datetime import datetime, timedelta
import json
import os
import datetime 
from itertools import pairwise
from record_time_script import time_spent_to_string,get_session_boot_time
from record_time_script import get_time_boot_or_timespent,calc_time_spent, string_to_timedelta
import subprocess


def create_files(directory_path="time_sessions_history", 
                 filename="time_spent_session_history.json") -> None:
    '''
    Creates the files structure to the sessions history
    '''
    WRITE_DIR_PERM = 0o755 
    print(f"{create_files.__name__} executed!!!")
    if not os.path.exists(directory_path):
        try:
            print("Current working directory before change: ", os.getcwd())

            # Change the current working directory
            #s.chdir('/path/to/directory')

            # Print the current working directory after the change
            #print("Current working directory after change: ", os.getcwd())
            os.makedirs(directory_path,mode=WRITE_DIR_PERM)
            # create respective file session
        
            if not os.path.exists("time_spent_session_history.json"):
                with open(f"{directory_path}/{filename}", "w") as file:
                    json.dump({"today_sessions":[], 
                            "last_seven_days_sessions":[],
                            "last_thirty_days_sessions":[]}, file, indent=8)
        except Exception as e:
             print(str(e))   
        else:
            print(f"{filename} exist!!!")
    else:
        print("The folder already exist!!!")
        return None

def stack_time_session(current_session_time, dir_name="time_sessions_history", 
                       filename="time_spent_session_history.json"):
    '''
    update the history of time spent
    '''
    print(f"{stack_time_session.__name__} executed!!!")
    current_time = datetime.datetime.now()
    today_date = current_time.strftime("%Y-%m-%d")

    # add todays time
    with open(f"{dir_name}/{filename}", "r") as history_dict:
        loaded_history_dict = json.load(history_dict)

        try:
            loaded_history_dict["today_sessions"].append(current_session_time)
            print(loaded_history_dict)
            
            with open(f"{dir_name}/{filename}", "w") as updated_dict:
                json.dump(loaded_history_dict, updated_dict, indent=8)
                
        except Exception as e:
            print(e)


def update_sessions_history(directory_path="time_sessions_history", 
                            filename="time_spent_session_history.json"):
    """
    Update the session's group based on their date

    @today_date - a temporary parameter for testing purposes

    """
   
    # does the today_sessions list has any item out of date?
    with open(f"{directory_path}/{filename}") as file:
        history_dict = json.load(file)
        today_date = datetime.datetime.now()
        today_date.date()

        deleted_sessions_today = []
        for session in history_dict["today_sessions"]:
            
            splitted = session.split(",")
            splitted = splitted[2].split(" ")
            splitted = splitted[1]
            
            splitted = splitted.split("-")
            splitted = [int(item) for item in splitted]
           
            session_date = datetime.date(year=splitted[0], 
                                         month=splitted[1],
                                          day=splitted[2])
            
            deltatime_item_now = today_date.date() - session_date
            print(f"deltatime_item_now:{deltatime_item_now.days}")
            # if it does, move those items to the week list     
            if today_date.day != 0:
                temp = session
                deleted_sessions_today.append(temp)
                history_dict["last_seven_days_sessions"].insert(0, temp)
        # cleaning up the today key
        for deleted_session in deleted_sessions_today:
            history_dict["today_sessions"].remove(deleted_session)

        with open(f"{directory_path}/{filename}", "w") as updated_file:
            json.dump(history_dict, updated_file, indent=8)
    # does the week_sessions list has any item has a deltatime == today_date - item_date > 7?
        # if it does, move those items to the month list
    # does the delete_sessions list has any item  deltatime == today_date - item_date > 30?
        # if it does, delete those items

def save_today_time_sessions(time_spent: str) -> None:
    '''
    Add the given time to the the today key
    '''

def save_week_time_sessions():
    '''
    Add the given time to the the week key
    '''

def save_month_time_sessions():
    '''
    Add the given time to the the week key
    '''