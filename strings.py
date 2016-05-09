from datetime import datetime

I_FLAG = str(datetime.now()) + " [INFO] "
I_GET_BROWSER_PROG = I_FLAG + "Checking for %s support."
I_GET_BROWSER_SUPPORT = I_FLAG + "Found %s in PATH!"
I_GET_BROWSER_NSUPPORT = I_FLAG + "%s was not found."
I_CAL_UPDATE_TASK = I_FLAG + "Running calendar update task."
I_CAL_CLEAR = I_FLAG + "Clearing previous events."
I_CAL_UPDATE_INSERT = I_FLAG + "Pushing event: %s - %s"
I_TASK_RUN = I_FLAG + "Running task: %s"
I_TASK_RUN_COMPLETE = I_FLAG + "Task complete: %s"
I_BROWSERTASK_COMMIT = I_FLAG + "Committing result to db: %s at %s"
I_SCRIPTTASK_COMMIT = I_FLAG + "Committing result to db: %s at %s"
I_THROWUP_START = I_FLAG + "Outputting HTML."
I_UPDATE_CRED_NEW_COUNT = I_FLAG + "%s new credentials added to db."

W_FLAG = str(datetime.now()) + " [WARN] "

E_FLAG = str(datetime.now()) + " [ERROR] "
E_GET_BROWSER_NONE = E_FLAG + """No compatible browsers were found in PATH! 
Please install one of the following:"""
E_BROWSERTASK_NO_BROWSERS = E_FLAG + "No browsers inited to run task: %s"
E_BROWSERTASK_NO_SETUP_FUNC = E_FLAG + "No setup_func defined for task: %s"
E_BROWSERTASK_NO_RUN_FUNC = E_FLAG + "No run_func defined for task: %s"
E_SCRIPTTASK_NO_SETUP_FUNC = E_FLAG + "No setup_func defined for task: %s"
E_SCRIPTTASK_NO_RUN_FUNC = E_FLAG + "No run_func defined for task: %s"
