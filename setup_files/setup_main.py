import config_execute_at_shutdown_perm 
import create_task_at_logon
import disable_fast_startup


if __name__ == "__main__":
    user_monitor_task = create_task_at_logon.TaskCreater()

    user_monitor_task.register_task(**{"author": "Use Monitor", 
                                  "descrip": "Execute a script that saves the current session time plus additional info"
                                  })

    fbd = config_execute_at_shutdown_perm.PolicyCreater()
    fbd.enable_policy()
    
    fbu = disable_fast_startup.FastBootDisabler()
    fbu.disable_fast_startup()
