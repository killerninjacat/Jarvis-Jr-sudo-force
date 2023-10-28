import typer
import random
import time
import os


app = typer.Typer()

def tossCoin():
    print(random.choice(["H", "T"]))

def find_audio_folders(search_path):
    command = (
        f"find {search_path} -type f -exec file --mime-type {{}} + | "
        "grep -E 'audio/(mp3|wav|flac)' | cut -d: -f1 | sort -u"
    )
    try:
        result = os.popen(command).read()
        folders = result.strip().split('\n')
        return folders
    except Exception as e:
        print(f"Error: {e}")
        return None

def playMusic():
    music_folder_current_user = os.path.join(os.path.expanduser("~"))
    print("Music Folder for Current User:", music_folder_current_user)
    print("Searching for media files...")
    
    files = os.listdir(music_folder_current_user)
    for foldername, subfolders, filenames in os.walk(music_folder_current_user):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            files.append(file_path)

    audio_file_extensions = ['.mp3', '.wav', '.flac', '.mp4', '.mkv', '.webm', '.mov']
    audio_files = [file for file in files if any(file.lower().endswith(ext) for ext in audio_file_extensions)]
    audio_files = sorted(audio_files, key=lambda x: os.path.getmtime(os.path.join(music_folder_current_user, x)), reverse=True)

    for file in audio_files:
        print(file)

    while True:
        verify_folder = input("Choose a different folder? (y/n)")
        if verify_folder.lower() == "y":
            music_folder_current_user = input("Enter the path to your music folder: ")
            '''
            print("Searching for audio files...")
            audio_folders = find_audio_folders("/home/nithin/")
            if audio_folders is not None:
                print("Folders containing audio files:")
                for folder in audio_folders:
                    print(folder)
                folder_index = int(input("Enter the index of the folder you want to play music from: "))
                music_folder_current_user = audio_folders[folder_index]
            else:
                print("audio_folders is None")
            '''
            files = os.listdir(music_folder_current_user)
            files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(music_folder_current_user, x)), reverse=True)
            for file in files:
                print(file)
        else:
            break

    file_index = int(input("Enter the index of the file you want to play: "))
    if os.name == 'nt':
        os.startfile(os.path.join(music_folder_current_user, files[file_index]))
    elif os.name == 'posix':
        file_path = os.path.join(music_folder_current_user, files[file_index])
        quoted_file_path = f'"{file_path}"'
        command = f"open {quoted_file_path}"
        os.system(command)
    else:
        print("Platform not recognized.")
    

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

    
