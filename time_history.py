from datetime import datetime, timedelta
import json
import os
import datetime 
from itertools import pairwise
from time_session_utility import time_spent_to_string,get_session_boot_time
from time_session_utility import get_time_boot_or_timespent,calc_time_spent, string_to_timedelta
from time_session_utility import load_dict_hist, write_dict_hist
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
        
            if not os.path.exists(filename):
                write_dict_hist({"today_sessions":[], 
                             "last_seven_days_sessions":[],
                             "last_thirty_days_sessions":[]})
                
            else:
                print(f"The file time_spent_session_history")
        except Exception as e:
             print(str(e))   
        else:
            print(f"{filename} exist!!!")
    else:
        print("The folder already exist!!!")

        if not os.path.exists(filename):
                write_dict_hist({"today_sessions":[], 
                             "last_seven_days_sessions":[],
                             "last_thirty_days_sessions":[]})
        return None

# def stack_time_session(current_session_time, dir_name="time_sessions_history", 
#                        filename="time_spent_session_history.json"):
#     '''
#     update the history of time spent
#     '''
#     print(f"{stack_time_session.__name__} executed!!!")
#     current_time = datetime.datetime.now()
#     today_date = current_time.strftime("%Y-%m-%d")

#     # add todays time
#     loaded_history_dict = load_dict_hist(load_whole_dict=True)

#     try:
#         loaded_history_dict["today_sessions"].append(current_session_time)
#         print(loaded_history_dict)
        
#         with open(f"{dir_name}/{filename}", "w") as updated_dict:
#             json.dump(loaded_history_dict, updated_dict, indent=8)
            
#     except Exception as e:
#         print(e)


def update_sessions_history(directory_path="time_sessions_history", 
                            filename="time_spent_session_history.json"):
    """
    Update the session's group based on their date

    @today_date - a temporary parameter for testing purposes

    """
    print(f"{update_sessions_history.__name__} executed!!!")

    # does the today_sessions list has any item out of date?

    history_dict = load_dict_hist(load_dict_hist=True)
    
    today_date = datetime.datetime.now()
    # clean repeated sessions
    history_dict["today_sessions"] = list(set(history_dict["today_sessions"]))
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
        if deltatime_item_now.days != 0:
            temp = session
            deleted_sessions_today.append(temp)
            history_dict["last_seven_days_sessions"].insert(0, temp)
    
    # cleaning up the today key
    for deleted_session in deleted_sessions_today:
        history_dict["today_sessions"].remove(deleted_session)

    # does the delete_sessions list has any item  deltatime == today_date - item_date  > 7?
        # if it does, delete those items
        deleted_sessions_week = []
        for session in history_dict["last_seven_days_sessions"]:
            
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
            if deltatime_item_now.days != 0:
                temp = session
                deleted_sessions_today.append(temp)
                history_dict["last_seven_days_sessions"].insert(0, temp)
        
        # cleaning up the today key
        for deleted_session in deleted_sessions_today:
            history_dict["today_sessions"].remove(deleted_session)

    # does the delete_sessions list has any item  deltatime == today_date - item_date  > 7?
        # if it does, delete those items
        deleted_sessions_week = []
        for session in history_dict["last_seven_days_sessions"]:
                    
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
                    if deltatime_item_now.days > 7:
                        temp = session
                        deleted_sessions_week.append(temp)
                        history_dict["last_thirty_days_sessions"].insert(0, temp)
                    # cleaning up the today key
        
        for deleted_session in deleted_sessions_week:
            history_dict["last_seven_days_sessions"].remove(deleted_session)

    # does the delete_sessions list has any item  deltatime == today_date - item_date > 30?
        # if it does, delete those items
        deleted_sessions_month = []
        for session in history_dict["last_thirty_days_sessions"]:
                    
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
        
                    # if it does, delete them     
                    if deltatime_item_now.days > 30:
                        deleted_sessions_month.append(session)
                        
                    # cleaning up the today key
        for deleted_session in deleted_sessions_month:
            history_dict["last_thirty_days_sessions"].remove(deleted_session)
        
        write_dict_hist(history_dict)

def save_session(time_spent: str, history_key="today_sessions",
                directory_path="time_sessions_history", 
                filename="time_spent_session_history.json") -> None:
    '''

    Add the given time to the the given history subset
    @time_unity: today_sessions, last_seven_days_sessions

    '''
    print(f"{save_session.__name__} executed!!!")
    file_path = f"{directory_path}/{filename}"
    
    if os.path.exists(file_path):
        try:
            history_dict = load_dict_hist(load_whole_dict=True)
        
            time_spent_str = time_spent_to_string(time_spent, include_date=True)

            # add boot time for duplicates verification
            boot_time: datetime = get_session_boot_time()
            time_spent_str += f", BOOT_TIME:{str(boot_time)}"

            history_dict[history_key].insert(0, time_spent_str) 

            
            write_dict_hist(history_dict)
      

        except Exception as e:
             print(str(e))

def calc_session_total_time(return_as_string=False,
                            history_key="today_sessions",
                            directory_path="time_sessions_history", 
                            filename="time_spent_session_history.json"):
    '''
    Calculates the sum of delta time of all items in a list.

    Obs.:This function is suppouse to be executed after the sessions rearrange
    '''
    print(f"{calc_session_total_time.__name__} executed!!!")

    
    file_path = f"{directory_path}/{filename}"

    total_session_time = {
         "days": 0,
         "hours":0,
         "minutes":0,
         "seconds":0
    }
    
    # open the file
    dict_hist = load_dict_hist(load_whole_dict=True)
   
    for item in dict_hist[history_key]:
        # convert all to deltatime
        delta_item = string_to_timedelta(item)

        # Accumulate timedelta values into total_session_time
        total_session_time["days"] += delta_item.days
        total_session_time["hours"] += delta_item.seconds // 3600
        total_session_time["minutes"] += (delta_item.seconds % 3600) // 60
        total_session_time["seconds"] += delta_item.seconds % 60

    # sum and return 
    if return_as_string:
         return time_spent_to_string(datetime.timedelta(days=total_session_time["days"],
                                   hours=total_session_time["hours"],
                                   minutes=total_session_time["minutes"],
                                   seconds=total_session_time["seconds"]), include_date=True)
    return total_session_time

def calc_last_seven_days_total(return_as_string=False):
     """
     Use calc_session_total_time to get the last seven days total time spent
     """
     today = calc_session_total_time()
     this_week = calc_session_total_time(history_key="last_seven_days_sessions")
     result = datetime.timedelta(days=today["days"] + this_week["days"],
                                 hours=today["hours"] + this_week["hours"],
                                 minutes=today["minutes"] + this_week["minutes"],
                                 seconds=today["seconds"] + this_week["seconds"],
                                 
                                 )
     if return_as_string:
          return time_spent_to_string(result)
     return result

def calc_last_thirty_days_total(return_as_string=False):
     """
     Use calc_session_total_time to get the last thirty days total time spent
     """
     this_week = calc_last_seven_days_total()
     this_month = calc_session_total_time(history_key="last_seven_days_sessions")
     result = datetime.timedelta(days=this_week.days + this_month["days"],
                                 hours=this_week.seconds // 3600 + this_month["hours"],
                                 minutes=(this_week.seconds % 3600) // 60 + this_month["minutes"],
                                 seconds=this_week.seconds % 60 + this_month["seconds"],
                                 )
     if return_as_string:
          return time_spent_to_string(result)
     return result

def get_time_from_sessions_total(time_string):
    """
    Splits and extract the time from a datetime object return by 'calc_session_total_time'
     
    """
    tmp = time_string.split(",")
    print(f"check:{tmp}")
    return ",".join(tmp[:2])

def calc_total_time():
    """
    calculate the sum of all sessions 
    """
    print(f"{calc_total_time.__name__} executed!!!")

    dict_keys = ["today_sessions", "last_seven_days_sessions", 
                 "last_thirty_days_sessions"]
    
    total_sum =  {
         "days":0,
         "hours":0,
         "minutes":0,
         "seconds":0
    }

    for key in dict_keys:
        curr_semitotal: dict = calc_session_total_time(history_key=key)

        total_sum["days"] += curr_semitotal["days"]
        total_sum["hours"] += curr_semitotal["hours"]
        total_sum["minutes"] += curr_semitotal["minutes"]
        total_sum["seconds"] += curr_semitotal["seconds"]

    # balance time
    remaining_time = int(total_sum["seconds"] / 60)
    total_sum["seconds"] = int(total_sum["seconds"] % 60)
    total_sum["minutes"] += int(remaining_time)

    remaining_time = int(total_sum["minutes"] / 60,) 
    total_sum["minutes"] = int(total_sum["minutes"] % 60)
    total_sum["hours"] += remaining_time

    remaining_time = int(total_sum["hours"] / 24)
    total_sum["minutes"] = int(total_sum["hours"] % 24)
    total_sum["hours"] += remaining_time

    return total_sum

def verify_duplicates(history_key="today_sessions",
                    directory_path="time_sessions_history", 
                    filename="time_spent_session_history.json"):
    """
    delete session duplicates that were recorded in the session (by checking their boot time)
    

    """
    file_path: str = f"{directory_path}/{filename}"
    print("")
    print(f"{calc_total_time.__name__} executed!!!")

    if os.path.exists(file_path):
        acum = 0
        # load the given history list
        history_dict = load_dict_hist(load_whole_dict=True)
        choosen_hist_list = history_dict[history_key]
        print(f"INPUT:{len(history_dict[history_key])}")
        duplicated_sessions = []
        if len(choosen_hist_list) >= 2:

            for current_sess, scssr_sess in pairwise(history_dict[history_key]):
                acum+=1
                # check the boot time
                dt_curr_sess = get_time_boot_or_timespent(current_sess)
                dt_scssr_sess = get_time_boot_or_timespent(scssr_sess)

                if dt_curr_sess == dt_scssr_sess:
                        duplicated_sessions.append(current_sess)

                # print(f"curr:{dt_curr_sess}\nscssr:{dt_scssr_sess}")

            # print(f"CHECK:{duplicated_sessions is choosen_hist_list}")
            # print(f"DUPLICATED SESSIONS:{duplicated_sessions}")

            
            for duplicated in duplicated_sessions:
                history_dict[history_key].remove(duplicated)

            
            #print(f"OUTPUT:{len(history_dict[history_key])}"
            
            write_dict_hist(history_dict)
        
        else:
                print("the given list has only one item, no need to verify it.")    
    else:
         raise Exception(f"{file_path} does not exist") 


def start():
     print(f"{start.__name__} executed!!!")

     create_files()
     update_sessions_history()
     time_spent: timedelta = calc_time_spent()
     save_session(time_spent)
     
     verify_duplicates()