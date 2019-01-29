import os
import sys
import tkinter

from bugme.controller import Controller

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class View:
    def __init__(self, root):
        self.change_note_frame = tkinter.Frame(root)
        self.on_off_frame = tkinter.Frame(root)
        self.frequency_frame = tkinter.Frame(root)
        self.utc_frame = tkinter.Frame(root)
        self.change_alert_frame = tkinter.Frame(root)
        self.token_change_frame = tkinter.Frame(root)
        self.changes_label = tkinter.Label(self.change_note_frame, text="Changes will take effect the next time BugMe is turned on")
        self.on_button = tkinter.Button(self.on_off_frame, text="ON", width=16, height=6)
        self.off_button = tkinter.Button(self.on_off_frame, text="OFF", width=16, height=6)
        self.frequency_label_1 = tkinter.Label(self.frequency_frame, text="Check and alert me every")
        self.frequency_input = tkinter.Entry(self.frequency_frame)
        self.frequency_label_2 = tkinter.Label(self.frequency_frame, text="minutes")
        self.offset_label = tkinter.Label(self.utc_frame, text="Change UTC Offset ('+' or '-' followed by time in HH:MM format)")
        self.offset_sign = tkinter.Listbox(self.utc_frame, selectmode="browse", width=3, height=2)
        self.offset_sign.insert(0, "+", "-")
        self.offset_amount = tkinter.Entry(self.utc_frame, width=10)
        self.change_alert_label = tkinter.Label(self.change_alert_frame, text="Change Alert Sound, provide a URI or browse your system for files")
        self.alert_uri = tkinter.Entry(self.change_alert_frame)
        self.alert_browse = tkinter.Button(self.change_alert_frame, width=8, text="Browse")
        self.change_token_label = tkinter.Label(self.token_change_frame, text="Change user token:")
        self.token_input = tkinter.Entry(self.token_change_frame, width=48, show="*")
        
        self.utc_frame.grid(row=0, column=0, padx=16, pady=16, sticky='nsew')
        self.offset_label.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.offset_sign.grid(row=1, column=0, sticky='nsew')
        self.offset_amount.grid(row=1, column=1, sticky='nsew')

        self.frequency_frame.grid(row=0, column=2, padx=16, pady=16, sticky='e')
        self.frequency_label_1.grid(row=0, column=0, sticky='nsew')
        self.frequency_input.grid(row=1, column=0, sticky='nsew')
        self.frequency_label_2.grid(row=1, column=1, sticky='nsew')

        self.change_alert_frame.grid(row=1, column=2, padx=16, pady=16, sticky='nsew')
        self.change_alert_label.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.alert_uri.grid(row=1, column=0, sticky='nsew')
        self.alert_browse.grid(row=1, column=1, sticky='nsew')

        self.on_off_frame.grid(row=2, column=1, padx=16, pady=16, sticky='nsew')
        self.on_button.grid(row=0, column=0, sticky='nsew')
        self.off_button.grid(row=0, column=1, sticky='nsew')

        self.token_change_frame.grid(row=1, column=0, padx=16, pady=16, sticky='nsew')
        self.change_token_label.grid(row=0, column=0, sticky='nsew')
        self.token_input.grid(row=1, column=0, sticky='nsew')

        self.change_note_frame.grid(row=2, column=0, padx=16, pady=16, sticky='nsew')
        self.changes_label.grid(row=0, column=0, sticky='w')

        self.on_button.bind('<Button-1>', Controller.turn_on)
        self.off_button.bind('<Button-1>', Controller.turn_off)
