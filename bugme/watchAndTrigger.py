from overdueAlert import play_alert
from getDueDates import *
from datetime import datetime, timedelta
from time import sleep
import json
from gui import *

"""What I need from GUI

- The UTC offset sign [o]
- The UTC offset amount [o]
- The User Token [o]
- Remind Frequency [o]
"""


utc_offset = offset_amount.get() # from gui
utc_sign = offset_sign.get() # from gui

with open('./bugme/tokens.json') as json_file:
    data = json.load(json_file)
    myKey = data['myAPIkey']

def trigger(utc_offset, utc_sign):
    """Goes through list of converted dates and compares them to current time to see if they have passed.
    
    Will be called after getDueDates's functions periodically as app is open to check to see if anything is overdue.
    """
    with open('./bugme/converted_dates.txt') as date_file:
        for date in date_file:
            if utc_sign == '-': 
                if str(datetime.now()+timedelta(hours=utc_offset[0:2], minutes=utc_offset[3:5])) > (date):
                    play_alert('./bugme/alert.mp3')
                    break
            elif utc_sign == '+':
                if str(datetime.now()-timedelta(hours=utc_offset[0:2], minutes=utc_offset[3:5])) > (date):
                    play_alert('./bugme/alert.mp3')
                    break


def watch():
    """Where it all happens, calls all relevant functions to check and respond to due status

    Goes through the process of getting and converting the due dates of each task,
    then testing them to see if they are past due. If they are past due trigger() will call
    the play_alert() function. Runs as long as app is up, will update and check
    tasks every ten minutes.
    """
    while True:
        get_due_dates(token_input.get())
        convert_dates()
        trigger()
        sleep(frequency_input.get() * 60) # Sleep for (10) minutes

