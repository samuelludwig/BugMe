import tkinter
from controller import *
window = tkinter.Tk()

def turn_on():
    token = token_input.get()
    frequency = frequency_input.get()
    offset = offset_amount.get()
    sign = offset_sign.curselection()
    uri = alert_uri.get()
    controller.watch(token, frequency, offset, sign, uri)

def turn_off():
    pass

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
on_button = tkinter.Button(on_off_frame, text="ON", width=16, height=6,command=turn_on)

# [Button] OFF
off_button = tkinter.Button(on_off_frame, text="OFF", width=16, height=6, command=turn_off)

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

window.mainloop()


#---------------------LAYOUT---------------------#
# [Title] Window Title
#
# [Label] Changes will take effect the next time BugMe
#           is turned ON
#
# [Button] ON
# [Button] OFF
#
# [Label] Check and Alert Me Every...
# [TextEntry] Alert Frequency Setting (>= 1 minute)
# [Label] ...minute(s)
#
# [Label] Change UTC Offset
# UTC Offset Field (Two Parts):
#   - [ListBox] POS/NEG Indicator
#   - [TextEntry] Time Offset in HH:MM Format
#
# [TextEntry] Change Alert Audio (Link)
#   + [Button] Browse for Soundfile on System
#
# [Label] Change User Token:
# [TextEntry] User Token