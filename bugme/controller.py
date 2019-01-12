import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from bugme import overdueAlert
from bugme import getDueDates
from bugme import gui
from datetime import datetime, timedelta
from time import sleep
import tkinter
import json

#################################################################################################
# TODO: Find a way to call watch repeatedly, which also stops when the off button is pressed    #
#################################################################################################
#                                                                                               # 
#################################################################################################

window = tkinter.Tk()
# [Title] Window Title
window.title("BugMe Control Panel")

# [Frame] Changes Note Component Container - Holds:
#   - [Label] Changes will take effect the next time BugMe is turned ON
change_note_frame = tkinter.Frame(window)

# [Frame] ON/OFF Component Container - Holds:
#   - [Button] ON
#   - [Button] OFF
on_off_frame = tkinter.Frame(window)

# [Frame] Alert Frequency Component Containter - Holds:
#   - [Label] Check and Alert Me Every...
#   - [TextEntry] Alert Frequency Setting (>= 1 minute)
#   - [Label] ...minute(s)
frequency_frame = tkinter.Frame(window)

# [Frame] UTC Component Container - Holds:
#   - [Label] Change UTC Offset
#   - [ListBox] POS/NEG Indicator
#   - [TextEntry] Time Offset in HH:MM Format
utc_frame = tkinter.Frame(window)

# [Frame] Change Alert Audio Component Container - Holds:
#   - [Label] Change Alert Sound
#   - [TextEntry] Change Alert Audio (URI)
#   - [Button] Browse for Soundfile on System
change_alert_frame = tkinter.Frame(window)

# [Frame] Token Change Component Container - Holds:
#   - [Label] Change User Token
#   - [TextEntry] User Token
token_change_frame = tkinter.Frame(window)


# [Label] Changes will take effect the next time BugMe is turned ON
changes_label = tkinter.Label(change_note_frame, text="Changes will take effect the next time BugMe is turned on")

# [Button] ON
on_button = tkinter.Button(on_off_frame, text="ON", width=16, height=6)

# [Button] OFF
off_button = tkinter.Button(on_off_frame, text="OFF", width=16, height=6)

# [Label] Check and Alert Me Every...
frequency_label_1 = tkinter.Label(frequency_frame, text="Check and alert me every")

# [TextEntry] Alert Frequency Setting (>= 1 minute)
frequency_input = tkinter.Entry(frequency_frame)

# [Label] ...minute(s)
frequency_label_2 = tkinter.Label(frequency_frame, text="minutes")

# [Label] Change UTC Offset
offset_label = tkinter.Label(utc_frame, text="Change UTC Offset ('+' or '-' followed by time in HH:MM format)")

# [ListBox] POS/NEG Indicator
offset_sign = tkinter.Listbox(utc_frame, selectmode="browse", width=3, height=2)
offset_sign.insert(0, "+", "-")

# [TextEntry] Time Offset in HH:MM Format
offset_amount = tkinter.Entry(utc_frame, width=10)

# [Label] Change Alert Sound
change_alert_label = tkinter.Label(change_alert_frame, text="Change Alert Sound, provide a URI or browse your system for files")

# [TextEntry] Change Alert Audio (URI)
alert_uri = tkinter.Entry(change_alert_frame)

# [Button] Browse for Soundfile on System
alert_browse = tkinter.Button(change_alert_frame, width=8, text="Browse")

# [Label] Change User Token
change_token_label = tkinter.Label(token_change_frame, text="Change user token:")

# [TextEntry] User Token
token_input = tkinter.Entry(token_change_frame, width=48, show="*")


utc_frame.grid(row=0, column=0, padx=16, pady=16, sticky='nsew')
offset_label.grid(row=0, column=0, columnspan=2, sticky='nsew')
offset_sign.grid(row=1, column=0, sticky='nsew')
offset_amount.grid(row=1, column=1, sticky='nsew')

frequency_frame.grid(row=0, column=2, padx=16, pady=16, sticky='e')
frequency_label_1.grid(row=0, column=0, sticky='nsew')
frequency_input.grid(row=1, column=0, sticky='nsew')
frequency_label_2.grid(row=1, column=1, sticky='nsew')

change_alert_frame.grid(row=1, column=2, padx=16, pady=16, sticky='nsew')
change_alert_label.grid(row=0, column=0, columnspan=2, sticky='nsew')
alert_uri.grid(row=1, column=0, sticky='nsew')
alert_browse.grid(row=1, column=1, sticky='nsew')

on_off_frame.grid(row=2, column=1, padx=16, pady=16, sticky='nsew')
on_button.grid(row=0, column=0, sticky='nsew')
off_button.grid(row=0, column=1, sticky='nsew')

token_change_frame.grid(row=1, column=0, padx=16, pady=16, sticky='nsew')
change_token_label.grid(row=0, column=0, sticky='nsew')
token_input.grid(row=1, column=0, sticky='nsew')

change_note_frame.grid(row=2, column=0, padx=16, pady=16, sticky='nsew')
changes_label.grid(row=0, column=0, sticky='w')

def turn_on(event):
    print("On button pressed!")
    grab_user_data(token_input.get(), frequency_input.get(), offset_amount.get(), offset_sign.curselection(), alert_uri.get())


def turn_off(event):
    pass

on_button.bind('<Button-1>', turn_on)
off_button.bind('<Button-1>', turn_off)

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
    tasks every x minutes.
    """
    getDueDates.get_due_dates(token)
    getDueDates.convert_dates()
    trigger(utc_offset, utc_sign, alert_uri)
    sleep(int(frequency) * 60) # Sleep for (frequency) minutes

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

def start():
    """Called when application is started, fills all text fields with whats in user_data.json 
    
    (if there is anything in that file)
    """
    pass


if __name__ == "__main__":
    window.mainloop()
    start()

# while True:
#     watch("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "1", "05:00", "-", "./bugme/alert.mp3") # <- test method of watch()

