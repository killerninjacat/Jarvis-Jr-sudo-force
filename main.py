import click
import requests
import openai
import os
import tictactoeai
import functions
from rich import print
from speech import say


from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

custom_style = Style.from_dict({
    'prompt': 'fg:#ff0066',
    'input': 'fg:#ff0066',
    'output': '#00ff00',
})

session = PromptSession(style=custom_style)


def get_platform():
    if os.name == 'nt':
        return 'Windows'
    elif os.name == 'posix':
        return 'macOS/Linux'
    else:
        return 'Unknown'

platform = get_platform()

def get_default_terminal():
    if platform == "Windows":
        return "cmd"
    elif platform == "macOS/Linux":
        return "Shell"

default_terminal = get_default_terminal()
openai.api_key="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"

def hello(name):
    click.echo("Hello "+name)

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":f"reply only with the {default_terminal} command to do the following\n\n"+prompt}]
    )
    return response.choices[0].message.content.strip()
    # return "fuck you"

    

def process_command(command):
    if ("tictactoe" in command) or ("tic tac toe") in command:
        os.system("clear")
        tictactoeai.init()
        return
        
    if (command in ["toss", "flip"]) and ("coin" in command):  #check
        os.system("clear")
        functions.tossCoin()
        return

    if ("date" in command) or ("time" in command):
        functions.dateAndTime(command)
        return

    if (command in ["stopwatch", "stop watch"] ):
        functions.stopwatch()
        return

    if("weather" in command):
        output = requests.get("https://www.wttr.in")
        city=""
        if("not found" in str(output.content)):
            print("Sorry, not sure of your current city")
            city = input("Enter your current city: ")
        os.system("curl wttr.in/"+city)
        return

    if ("countdown" in command) or ("timer" in command):
        time = chat_with_gpt(f"below given sentence is a user generated sentence. find how long the timer should run, convert it to seconds and reply with only that message\n\n"+command)
        # k = command.split()
        # s =  int(k[-2])
        functions.countdown(time)
        return
    
    cmd = chat_with_gpt(f"extract the default terminal name from {default_terminal} reply only with the {default_terminal} command to do the following\n\n"+command)
    folderName = "folder_name"
    fileName = "file_name"
    if("folder_name" in cmd):
        folderName = input("Enter a folder name ")
    if("file_name" in cmd):
        fileName = input("Enter a file name ")
        cmd.replace("file_name", fileName)
    elif("file" in cmd):
        fileName = input("Enter a file name ")
        cmd.replace("file", fileName)
    cmd = cmd.replace("folder_name", folderName)
    res = os.system(cmd)
    say("Action performed successfully")

    print(cmd , res)

while True:
    user_input = session.prompt("Enter your command in plain English: ")



    # user_input = session.prompt("Enter your command in plain English: ")
    
    process_command(user_input)
    ask_for_another = input("Do you want to perform another operation? (yes/no): ")
    if ask_for_another.lower() != "yes":
        print("Exiting...")
        break


