import json
from todoist.api import TodoistAPI
with open('./bugme/tokens.json') as json_file:
    data = json.load(json_file)
    myKey = data['myAPIkey']
api = TodoistAPI(myKey)
api.sync()
print(api.state['projects'])
