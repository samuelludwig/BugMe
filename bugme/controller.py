from bugme import overdueAlert
from bugme import getDueDates
from datetime import datetime, timedelta
from time import sleep

#################################################################################################
# TODO: Find a way to call watch repeatedly, which also stops when the off button is pressed    #
#################################################################################################
#                                                                                               # 
#################################################################################################

# def turn_on():
#     token = token_input.get()
#     frequency = frequency_input.get()
#     offset = offset_amount.get()
#     sign = offset_sign.curselection()
#     uri = alert_uri.get()
#     profile = controller.Controller(token, frequency, offset, sign, uri)
#     profile.watch(token, frequency, offset, sign, uri)

# def turn_off():
#     pass

class Controller:
    def __init__(self, token, frequency, utc_offset, utc_sign, alert_uri):
        self.token = token
        self.frequency = frequency
        self.utc_offset = utc_offset
        self.utc_sign = utc_sign
        self.alert_uri = alert_uri

def trigger(utc_offset, utc_sign, alert_uri):
        """Goes through list of converted dates and compares them to current time to see if they have passed.
        
        Will be called after getDueDates's functions periodically as app is open to check to see if anything is overdue.
        """
        with open('./bugme/converted_dates.txt') as date_file:
            for date in date_file:
                if utc_sign == '-': 
                    if str(datetime.now()+timedelta(hours=int(utc_offset[0:2]), minutes=int(utc_offset[3:5]))) > (date):
                        overdueAlert.play_alert(alert_uri)
                        break
                elif utc_sign == '+':
                    if str(datetime.now()-timedelta(hours=int(utc_offset[0:2]), minutes=int(utc_offset[3:5]))) > (date):
                        overdueAlert.play_alert(alert_uri)
                        break

def watch(token, frequency, utc_offset, utc_sign, alert_uri):
    """Where it all happens, calls all relevant functions to check and respond to due status

    Goes through the process of getting and converting the due dates of each task,
    then testing them to see if they are past due. If they are past due trigger() will call
    the play_alert() function. Runs as long as app is up, will update and check
    tasks every ten minutes.
    """
    getDueDates.get_due_dates(token)
    getDueDates.convert_dates()
    trigger(utc_offset, utc_sign, alert_uri)
    sleep(int(frequency) * 60) # Sleep for (frequency) minutes

# while True:
#     watch("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "1", "05:00", "-", "./bugme/alert.mp3") # <- test method of watch()

