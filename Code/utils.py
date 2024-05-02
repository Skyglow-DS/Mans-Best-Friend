import os
import shutil

def check_directory(folder, remove = False):
    if not os.path.exists(folder):
        print(f"Creating missing folder {folder}")
        try:
            os.makedirs(folder)     
        except OSError as e:
            raise OSError(f"Failed to create directory '{folder}': {e}")
    else:
        if remove:
            print(f"Removing and recreating existing folder and files in {folder}")
            try:
                shutil.rmtree(folder)  
                os.makedirs(folder)   
            except OSError as e:
                raise OSError(f"Failed to remove directory '{folder}': {e}")
        else:
            print(f"Folder already exists {folder}")
    return 

def move_files(original_path, new_path, verbose = False):
    print(f"Moving all files {original_path} to {new_path} ...")
    for file_name in os.listdir(original_path):
        original_file_path = os.path.join(original_path, file_name)
        new_file_path = os.path.join(new_path, file_name)
        if verbose:
            print(f"Moving {original_file_path} to {new_file_path} ...")
        shutil.move(original_file_path, new_file_path)

    if not os.listdir(original_path):
        print(f"Folder '{original_path}' is empty. Removing...")
        os.rmdir(original_path)
    return

def move_directory(original_path, new_path, verbose=False):
    print(f"Moving folder {original_path} to {new_path} ...")
    shutil.move(original_path, new_path)
    if verbose:
        print(f"Moved {original_path} to {new_path}")
    
    return

def remove_directory(folder):
    try:
        shutil.rmtree(folder)
    except OSError as e:
                raise OSError(f"Failed to remove directory '{folder}': {e}")

def find_key(dictionary, item):
    for key, values in dictionary.items():
        if item in values:
            return key
    return 