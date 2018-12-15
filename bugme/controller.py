from watchAndTrigger import watch
from getDueDates import *
import threading

is_on = False

##############################################################################################
# TODO: Find a way to call watch repeatedly, which also stops when the off button is pressed #
##############################################################################################

def watchThread(i):
    try:
        watch(token_input.get(), frequency_input.get(), offset_amount.get(), offset_sign.get(offset_sign.curselection()), alert_uri.get())
    except:
        print("calling watch failed")

watchMe = threading.Thread(target=watchThread, args=(0))

def turn_on():
    is_on = True
    try:
        watchMe.start()
        watchMe.join()
    except:
        print("Oh dear, something's gone terribly wrong...")

def turn_off():
    is_on = False