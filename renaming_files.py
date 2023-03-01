import os

def rename_files():
    folder_path = input("Enter folder path: ")
    remove_char = input("Enter character(s) to remove: ")
    prefix = input("Enter prefix (leave blank if not needed): ")
    suffix = input("Enter suffix (leave blank if not needed): ")
    replace_str = input("Enter string to replace (leave blank if not needed): ")
    replace_with = input("Enter string to replace with (leave blank if not needed): ")

    for file_name in os.listdir(folder_path):
        if remove_char in file_name:
            new_file_name = file_name.replace(remove_char, "")
        else:
            new_file_name = file_name

        if replace_str in new_file_name:
            new_file_name = new_file_name.replace(replace_str, replace_with)

        if prefix:
            new_file_name = prefix + new_file_name

        if suffix:
            new_file_name = new_file_name.split('.')[0] + suffix + '.' + new_file_name.split('.')[1]

        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

    print("Done")

rename_files()
