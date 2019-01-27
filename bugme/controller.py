import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from time import sleep
import json
import multiprocessing
import tkinter
from bugme import getDueDates, overdueAlert, view
from datetime import datetime, timedelta

### --- BEGIN UI COMPONENT DEFINITION --- ###

class Controller:
    def __init__(self):
        self.root = tkinter.Tk()
        self.view = view.View(self.root)
    #     self.root.on_button.bind('<Button-1>', self.turn_on)
    #     self.root.off_button.bind('<Button-1>', self.turn_off)

    # def turn_on(self, event):
    #     print("On button pressed!") # DEBUG PRINT: REMOVE THIS LATER #
    #     # grab_user_data(token_input.get(), frequency_input.get(), offset_amount.get(), offset_sign.curselection(), alert_uri.get())
    #     # watch_process.start()

    # def turn_off(self, event):
    #     print("Off button pressed!") # DEBUG PRINT: REMOVE THIS LATER #
    #     # watch_process.terminate()
    #     # watch_process.join()

    def run(self):
        self.root.title("BugMe Control Panel")
        self.root.deiconify()
        self.root.mainloop()

### --- END UI COMPONENTS --- ###

def trigger(utc_offset, utc_sign, alert_uri):
        """Goes through list of converted dates and compares them to current time to see if they have passed.
        
        Will be called after getDueDates's functions periodically as app is open to check to see if anything is overdue.
        """
        with open('./bugme/converted_dates.txt') as date_file:
            for date in date_file:
                if utc_sign == [1]: 
                    if str(datetime.now()+timedelta(hours=int(utc_offset[0:2]), minutes=int(utc_offset[3:5]))) > (date):
                        overdueAlert.play_alert(alert_uri)
                        break
                elif utc_sign == [0]:
                    if str(datetime.now()-timedelta(hours=int(utc_offset[0:2]), minutes=int(utc_offset[3:5]))) > (date):
                        overdueAlert.play_alert(alert_uri)
                        break
            
def fill_fields():
    """Takes data (if present) from user_data.json and fills it into view fields on app open
    
    If there is no data present, the fields will be empty
    """
    with open("./bugme/user_data.json", "r") as data_file:
        try:
            data = json.load(data_file)
            token_input.insert(0, data['user_info'][0]['token'])
            frequency_input.insert(0, data['user_info'][0]['frequency'])
            offset_amount.insert(0, data['user_info'][0]['utc_offset'])
            
            if(data['user_info'][0]['utc_sign'] == [1]):
                offset_sign.activate(0)
            else:
                offset_sign.activate(1)

            alert_uri.insert(0, data['user_info'][0]['alert_uri'])
        except:
            pass

def grab_user_data(token, frequency, utc_offset, utc_sign, alert_uri):
    """Tosses entered user data into a JSON file (user_data.json)
    
    Arguments:
        token {string} -- api key for user
        frequency {int} -- frequency of alerts/checks
        utc_offset {string} -- utc offset amount in HH:MM format
        utc_sign {char} -- sign of utc offset (+ or -)
        alert_uri {string} -- path to audio file to play alert
    """

    data = {}
    data["user_info"] = []
    data["user_info"].append({
        "token": token,
        "frequency": frequency,
        "utc_offset": utc_offset,
        "utc_sign": utc_sign,
        "alert_uri": alert_uri
    })
    with open("./bugme/user_data.json", "w") as data_file:
        json.dump(data, data_file)

def watch(token, frequency, utc_offset, utc_sign, alert_uri):
        """Where it all happens, calls all relevant functions to check and respond to due status

        Goes through the process of getting and converting the due dates of each task,
        then testing them to see if they are past due. If they are past due trigger() will call
        the play_alert() function. Runs as long as app is up, will update and check
        tasks every (frequency) minutes.
        """
        last_time = (datetime.now() - timedelta(minutes=int(frequency)))
        
        while True:
            if datetime.now() > last_time+timedelta(minutes=int(frequency)):
                last_time = datetime.now()
                getDueDates.get_due_dates(token)
                getDueDates.convert_dates()
                trigger(utc_offset, utc_sign, alert_uri)

if __name__ == "__main__":
    fill_fields()
    multiprocessing.set_start_method('spawn')
    with open("./bugme/user_data.json") as data_file:
        data = json.load(data_file)
        watch_process = multiprocessing.Process(target=watch, args=(
            data['user_info'][0]['token'],
            data['user_info'][0]['frequency'], 
            data['user_info'][0]['utc_offset'], 
            data['user_info'][0]['utc_sign'], 
            data['user_info'][0]['alert_uri']))

# call_watch_me()
# while True:
#     watch("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "1", "05:00", "-", "./bugme/alert.mp3") # <- test method of watch()

