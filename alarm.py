import beepy
import datetime

def alarm():
    current = datetime.datetime.now()
    min = int(input("Enter time in minutes from now where alarm will activate"))
    time_change = datetime.timedelta(minutes=min)
    new_time = current + time_change 
