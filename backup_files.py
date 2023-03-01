import os
import shutil

def backup_files():
    src_folder = input("Enter source folder path: ")
    dest_folder = input("Enter destination folder path: ")
    
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)

    for foldername, subfolders, filenames in os.walk(src_folder):
        for filename in filenames:
            src_file_path = os.path.join(foldername, filename)
            dest_file_path = os.path.join(dest_folder, os.path.relpath(src_file_path, src_folder))
            os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
            shutil.copy2(src_file_path, dest_file_path)

    print("Backup complete")

backup_files()
