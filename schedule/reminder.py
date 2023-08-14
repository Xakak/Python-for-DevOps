import schedule
import time

def break_reminder():
    print("You need to take a break.It's 2 Hours.")


schedule.every(2).minutes.do(break_reminder)

while True:
    schedule.run_pending()
    time.sleep(1)