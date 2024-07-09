from datetime import datetime
#status will tell us what to log either the movie wasnt found or was
#also the time the script was executed to make sure its running on time.



def logIt(status):
    logFile = open('resources/log', 'a')
    messageSuccess = 'Interstellar is finally availbe for advance tickets!!!!!!!!!!!'
    messageFail = 'Interstellar was Not found at Cinemarks website'
    current_time =  datetime.now()
    if(status):
        logFile.write(f"{current_time} - {messageSuccess} -\n")
    else:
        logFile.write(f"{current_time} - {messageFail} -\n")