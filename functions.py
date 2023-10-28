import typer
import random
import time


app = typer.Typer()

def tossCoin():
    print(random.choice(["H", "T"]))


def dateAndTime():
    '''
    if ("date" in commmand) and ("time" in command):
        print(time.strftime('%Y-%m-%d %H:%M:%S'), end='\r')
    elif ("date" in commmand):
        print(time.strftime('%Y-%m-%d'), end='\r')
    elif("time" in command):
        print(time.strftime('%H:%M:%S'), end='\r')
   '''
    while True:
        print(time.strftime('%Y-%m-%d %H:%M:%S'), end='\r')
        time.sleep(1)

import time

def countdown(seconds):
    start = int(time.time()) + seconds
    while start >= int(time.time()):
        remaining_time = start - int(time.time())
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(remaining_time))
        print(formatted_time, end='\r')
        time.sleep(0.1)

def stopwatch():
    start_time = int(time.time())
    while True:
        elapsed_time = int(time.time()) - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        print(formatted_time, end='\r')
        time.sleep(0.1)

#need to work on ending it

    
