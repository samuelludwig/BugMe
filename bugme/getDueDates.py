import datetime
import json
from todoist.api import TodoistAPI
with open('./bugme/tokens.json') as json_file:
    data = json.load(json_file)
    myKey = data['myAPIkey']

def get_due_dates(apiKey):
    api = TodoistAPI(apiKey)
    api.sync()
    tasklist = api.items.all()
    with open('./bugme/base_dates.txt', 'w') as base_file:
        for task in tasklist:
            try:
                base_file.write(task['due_date_utc'] + '\n')
            except:
                pass

def convert_dates():
    with open('./bugme/converted_dates.txt', 'w') as con_file:
        while con_file.readline():
            print()
    
    print()

get_due_dates(myKey)
convert_dates()
