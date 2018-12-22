from watchAndTrigger import watch
from getDueDates import *
import gui
import threading

is_on = False

#################################################################################################
# TODO: Find a way to call watch repeatedly, which also stops when the off button is pressed    #
# TODO: Figure out this unresolved imports nonsense                                             #
#################################################################################################
# Based on a stack overflow question:                                                           #
# https://stackoverflow.com/questions/45648082/get-argument-of-tkinter-instance-in-other-module #
# - Might have my import flow backwards, should have controller calling GUI and not the other   #
#   way around.                                                                                 #
# - Should call the input-ed fields in turn_on function defined here in controller              #
# - Will need to do some refactoring work but seems promising                                   # 
#################################################################################################

def watchThread(token, frequency, offset, offset_sign, alert_uri):
    try:
        global is_on
        while(is_on):
            watch(token, frequency, offset, offset_sign, alert_uri)
    except:
        print("calling watch failed")

def turn_on():
    global is_on
    is_on = True
    try:
        watchMe = threading.Thread(target=watchThread, args=(gui.token_input.get(), gui.frequency_input.get(), gui.offset_amount.get(), gui.offset_sign.get(), gui.alert_uri.get()))
        watchMe.start()
    except:
        print("Oh dear, something's gone terribly wrong...")

def turn_off():
    global is_on
    is_on = False