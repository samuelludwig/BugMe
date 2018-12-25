from overdueAlert import play_alert
from getDueDates import *
from datetime import datetime, timedelta
from time import sleep

#################################################################################################
# TODO: Find a way to call watch repeatedly, which also stops when the off button is pressed    #
# TODO: Figure out this unresolved imports nonsense                                             #
#################################################################################################
#                                                                                               # 
#################################################################################################

class controller: pass

def trigger(utc_offset, utc_sign, alert_sound):
    """Goes through list of converted dates and compares them to current time to see if they have passed.
    
    Will be called after getDueDates's functions periodically as app is open to check to see if anything is overdue.
    """
    with open('./bugme/converted_dates.txt') as date_file:
        for date in date_file:
            if utc_sign == '-': 
                if str(datetime.now()+timedelta(hours=int(utc_offset[0:2]), minutes=int(utc_offset[3:5]))) > (date):
                    play_alert(alert_sound)
                    break
            elif utc_sign == '+':
                if str(datetime.now()-timedelta(hours=int(utc_offset[0:2]), minutes=int(utc_offset[3:5]))) > (date):
                    play_alert(alert_sound)
                    break


def watch(token, frequency, utc_offset, utc_sign, alert_sound):
    """Where it all happens, calls all relevant functions to check and respond to due status

    Goes through the process of getting and converting the due dates of each task,
    then testing them to see if they are past due. If they are past due trigger() will call
    the play_alert() function. Runs as long as app is up, will update and check
    tasks every ten minutes.
    """
    get_due_dates(token)
    convert_dates()
    trigger(utc_offset, utc_sign, alert_sound)
    sleep(int(frequency) * 60) # Sleep for (frequency) minutes


