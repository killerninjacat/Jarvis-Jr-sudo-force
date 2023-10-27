import click
import requests
import openai
import os

openai.api_key="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"

def hello(name):
    click.echo("Hello "+name)

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":"reply only with the bash command to do the following\n\n"+prompt}]
    )
    return response.choices[0].message.content.strip()

def process_command(command):
    # if "delete a file" in command:
    #     file_name = input("Enter the file name to delete: ")
    #     print(f"Deleting file: {file_name}")
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