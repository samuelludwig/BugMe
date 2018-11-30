from overdueAlert import play_alert
from datetime import datetime

def trigger():
    """Goes through list of converted dates and compares them to current time to see if they have passed.
    
    Will be called after getDueDates functions periodically as app is open to check to see if anything is overdue.
    """
    with open('./bugme/converted_dates.txt') as date_file:
        for date in date_file:
            if str(datetime.now()) > (date):
                play_alert('./bugme/alert.mp3')
                break
