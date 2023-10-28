import typer
import random
import time


app = typer.Typer()

def tossCoin():
    print(random.choice(["H", "T"]))


def dateAndTime(command):

    if ("date" in command) and ("time" in command):
        print(time.strftime('%Y-%m-%d %H:%M:%S'), end='\r')
    elif ("date" in command):
        print(time.strftime('%Y-%m-%d'), end='\r')
    elif("time" in command):
        print(time.strftime('%H:%M:%S'), end='\r')
    else:
        print(time.strftime('%Y-%m-%d %H:%M:%S'), end='\r')
    print()


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

    
