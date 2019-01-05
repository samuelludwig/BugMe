# BugMe

App using todoist api to play audio on my desktop if I am late to complete a task.

## How to Use

- In its current iteration, the program can only be run manually
- To do this, you must know:
  - Your Todoist API key
  - Your timezones UTC offset

- Uncomment the "test" code on the bottom of the file `controller.py`
- Replace the feild of `xxxxxxxx...xxxx` with your api key
- Replace `05:00` with your UTC offset amount in HH:MM format
- Replace `-` with the sign of your UTC offset
- Replace `1` with the amount of minutes you want for it to wait before checking your tasks again
- Run the `controller.py` file

### Note

- The program will run continuously until it is manually stopped