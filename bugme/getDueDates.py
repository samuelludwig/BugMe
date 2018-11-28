import datetime
import json
from todoist.api import TodoistAPI
with open('./bugme/tokens.json') as json_file:
    data = json.load(json_file)
    myKey = data['myAPIkey']


def get_due_dates(apiKey):
    """Isolates due dates/times of all todoist tasks and writes them to a file (base_dates.txt)."""
    api = TodoistAPI(apiKey)
    api.sync()
    tasklist = api.items.all()
    with open('./bugme/base_dates.txt', 'w') as base_file:
        for task in tasklist:
            try:
                base_file.write(task['due_date_utc'] + '\n')
            except:
                pass


def convert_month(month):
    """Helper function for convert_dates(), converts text-month to int-style month"""
    return {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12',
        '': 'xx'
    }[month]


def convert_dates():
    """Changes dates to a date-timey layout that I can test against.

    Takes a line from base_dates.txt and converts it, then puts it into the converted_dates.txt.
    I can probably do this only using one file, for another time...
    Format coming in: Sat 01 Dec 2018 22:00:00 +0000
    Format going out: 2018-11-27 19:07:45.103349    
    """
    with open('./bugme/base_dates.txt', 'r') as base_file:
        with open('./bugme/converted_dates.txt', 'w') as con_file:
            for base_time in base_file:                                 # String should look like:
                con_time = base_time[11:15] + '-'                       # '2018-'
                con_time += (convert_month(base_time[7:10]) + '-')      # '2018-11-'
                con_time += (base_time[4:6] + ' ')                      # '2018-11-27 '
                con_time += (base_time[16:24] + '.')                    # '2018-11-27 19:07:45.
                con_time += ('000000' + '\n')                           # '2018-11-27 19:07:45.000000' <- rounds down microseconds

                con_file.write(con_time)
    pass

get_due_dates(myKey)
convert_dates()
