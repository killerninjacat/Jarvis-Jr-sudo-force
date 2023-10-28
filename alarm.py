import beepy
import datetime
import time
from threading import Thread

def set_alarm():
    current = datetime.datetime.now()
    min = int(input("Enter time in minutes from now where alarm will activate\n"))
    time_change = datetime.timedelta(minutes=min)
    new_time = current + time_change
    return new_time.strftime('%H:%M')

def alarm():
    t = set_alarm()
    while True:
        if  t == datetime.datetime.now().strftime('%H:%M'):
            while True:
                beepy.beep(sound=1)
                time.sleep(0.01)


