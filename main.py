import click
import requests
import json
import openai
import os
import tictactoeai
import functions
from rich import print
from listen import Listen
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
        return "bash"


default_terminal = get_default_terminal()
openai.api_key = "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"


prompt_template = """reply in the following format
{
\""""+default_terminal+""" command":\""""+default_terminal+""" command to perform the action(do not use "touch" in cmd command. use echo "" > to create a file).If all required details are provided, required details should be empty. Only if details like file name or folder name are not already provided, use <placeholder> in its place",
"required details":"list the <placeholder>s in the """+default_terminal+""" command here in the form of a python list(give only """+default_terminal+""" command )",
"summary":"very short summary of the action performed. the phrase must be in past tense"
} to perform the below action


"""

print(prompt_template)


def hello(name):
    click.echo("Hello "+name)


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def process_command(command):
    if not isinstance(command, dict):
        if ("tictactoe" in command) or ("tic tac toe") in command:
            os.system("clear")
            tictactoeai.init()
            return

        if (command in ["toss", "flip"]) and ("coin" in command):  # check
            os.system("clear")
            functions.tossCoin()
            return

        if ("date" in command) or ("time" in command):
            functions.dateAndTime(command)
            return

        if (command in ["stopwatch", "stop watch"]):
            functions.stopwatch()
            return

        if ("weather" in command):
            output = requests.get("https://www.wttr.in")
            city = ""
            if ("not found" in str(output.content)):
                print("Sorry, not sure of your current city")
                city = input("Enter your current city: ")
            os.system("curl wttr.in/"+city)
            # say("Showing weather results.. ohhhhhhhhhhh its coold")

            return

        if ("countdown" in command) or ("timer" in command):
            time = chat_with_gpt(
                f"below given sentence is a user generated sentence. find how long the timer should run, convert it to seconds and reply with only that message\n\n"+command)
            # k = command.split()
            # s =  int(k[-2])
            functions.countdown(time)
            return

    # cmd = chat_with_gpt(
    #     f"provide the {default_terminal} command and a very short summary of the action (dont include this in command and dont include 'command:' just the command for the first is enough and give the short summary in past tense). return all this as a object datatype(key must be command and summary only both must be in double quotes. command must be a {default_terminal} command) for the following\n\n"+command)
    # print(cmd)
    # os.system(cmd[default_terminal+" command"])
    # # if not (isinstance(cmd, dict)):
    # # cmd = json.loads(cmd)
    # print(cmd["summary"])

    # cmd = cmd["command"].replace("folder_name", folderName)
    # res = os.system(cmd["command"])
    # if (cmd["summary"]):
    #     say(cmd["summary"])

    cmd = chat_with_gpt(prompt_template+command)
    print(cmd)
    dictionary = eval(cmd)
    if ((isinstance(dictionary["required details"], list)) and len(dictionary["required details"]) != 0):
        print("Please fill the required details")
        for i in dictionary["required details"]:
            val = input(i+": ")
            print(dictionary[f"{default_terminal} command"])
            dictionary[f"{default_terminal} command"] = dictionary[f"{default_terminal} command"].replace(
                i, val)
    os.system(dictionary[f"{default_terminal} command"])
    if (dictionary["summary"]):
        say(dictionary["summary"])


while True:
    choice = input(
        "Click 1 to enter the command in plain english, Click 2 for Speech recognition")
    if (choice == "1"):
        user_input = session.prompt("Enter your command in plain English: ")
    else:
        user_input = Listen()

    # user_input = session.prompt("Enter your command in plain English: ")

    process_command(user_input)
    ask_for_another = input(
        "Do you want to perform another operation? (yes/no): ")
    if ask_for_another.lower() != "yes":
        print("Exiting...")
        break
