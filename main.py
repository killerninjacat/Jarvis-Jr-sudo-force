import click
import requests
import openai
import os
import tictactoeai

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
        return os.environ.get('ComSpec', 'cmd.exe')
    elif platform == "macOS/Linux":
        return os.environ.get('SHELL', '/bin/sh')

default_terminal = get_default_terminal()
# print("Default Terminal: ", default_terminal)
openai.api_key="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"

def hello(name):
    click.echo("Hello "+name)

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":f"extract the default terminal name from {default_terminal} reply only with the {default_terminal} command to do the following\n\n"+prompt}]
    )
    return response.choices[0].message.content.strip()

def process_command(command):
    if ("tictactoe" in command) or ("tic tac toe") in command:
        os.system("clear")
        tictactoeai.init()
        return
    cmd = chat_with_gpt(command)
    folderName = "folder_name"
    fileName = "file_name"
    if("folder_name" in cmd):
        folderName = input("Enter a folder name ")
    if("file_name" in cmd):
        fileName = input("Enter a file name ")
    
    cmd = cmd.replace("folder_name", folderName).replace("file_name", fileName)
    res = os.system(cmd)
    print(cmd , res)
    

while True:
    user_input = input("Enter your command in plain English: ")
    process_command(user_input)
    ask_for_another = input("Do you want to perform another operation? (yes/no): ")
    if ask_for_another.lower() != "yes":
        print("Exiting...")
        break