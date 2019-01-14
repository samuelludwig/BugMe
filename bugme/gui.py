import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import tkinter

from bugme import controller

controller.utc_frame.grid(row=0, column=0, padx=16, pady=16, sticky='nsew')
controller.offset_label.grid(row=0, column=0, columnspan=2, sticky='nsew')
controller.offset_sign.grid(row=1, column=0, sticky='nsew')
controller.offset_amount.grid(row=1, column=1, sticky='nsew')

controller.frequency_frame.grid(row=0, column=2, padx=16, pady=16, sticky='e')
controller.frequency_label_1.grid(row=0, column=0, sticky='nsew')
controller.frequency_input.grid(row=1, column=0, sticky='nsew')
controller.frequency_label_2.grid(row=1, column=1, sticky='nsew')

controller.change_alert_frame.grid(row=1, column=2, padx=16, pady=16, sticky='nsew')
controller.change_alert_label.grid(row=0, column=0, columnspan=2, sticky='nsew')
controller.alert_uri.grid(row=1, column=0, sticky='nsew')
controller.alert_browse.grid(row=1, column=1, sticky='nsew')

controller.on_off_frame.grid(row=2, column=1, padx=16, pady=16, sticky='nsew')
controller.on_button.grid(row=0, column=0, sticky='nsew')
controller.off_button.grid(row=0, column=1, sticky='nsew')

controller.token_change_frame.grid(row=1, column=0, padx=16, pady=16, sticky='nsew')
controller.change_token_label.grid(row=0, column=0, sticky='nsew')
controller.token_input.grid(row=1, column=0, sticky='nsew')

controller.change_note_frame.grid(row=2, column=0, padx=16, pady=16, sticky='nsew')
controller.changes_label.grid(row=0, column=0, sticky='w')

controller.start()
controller.window.mainloop()
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