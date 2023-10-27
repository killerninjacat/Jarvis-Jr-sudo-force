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
    res = os.system(cmd)
    print(cmd , res)
    

while True:
    user_input = input("Enter your command in plain English: ")
    process_command(user_input)
    ask_for_another = input("Do you want to perform another operation? (yes/no): ")
    if ask_for_another.lower() != "yes":
        print("Exiting...")
        break