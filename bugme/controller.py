from watchAndTrigger import watch
from getDueDates import *
import threading

is_on = False

##############################################################################################
# TODO: Find a way to call watch repeatedly, which also stops when the off button is pressed #
##############################################################################################

def watchThread(token, frequency, offset, offset_sign, alert_uri):
    try:
        global is_on
        while(is_on):
            watch(token, frequency, offset, offset_sign, alert_uri)
    except:
        print("calling watch failed")

def turn_on(token, frequency, offset, offset_sign, alert_uri):
    global is_on
    is_on = True
    try:
        watchMe = threading.Thread(target=watchThread, args=(token, frequency, offset, offset_sign, alert_uri))
        watchMe.start()
    except:
        print("Oh dear, something's gone terribly wrong...")

def turn_off():
    global is_on
    is_on = False