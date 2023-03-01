import os
import time

def monitor_folder():
    folder_path = input("Enter folder path: ")
    files = {}

    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            files[file_path] = os.stat(file_path).st_mtime

    while True:
        time.sleep(10)
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                if file_path not in files:
                    print(f"{file_path} added")
                    files[file_path] = os.stat(file_path).st_mtime
                elif files[file_path] != os.stat(file_path).st_mtime:
                    print(f"{file_path} modified")
                    files[file_path] = os.stat(file_path).st_mtime

        for file_path in list(files):
            if not os.path.exists(file_path):
                print(f"{file_path} deleted")
                del files[file_path]

monitor_folder()
