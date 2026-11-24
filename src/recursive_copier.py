import os
import shutil

def recursive_copier(old_directory, new_directory):
    for p in os.listdir(old_directory):
        full_path = os.path.join(old_directory, p)
        if os.path.isfile(full_path):
            shutil.copy(os.path.join(old_directory, p), os.path.join(new_directory, p))
        if os.path.isdir(full_path):
            new_path = os.path.join(new_directory, p)
            os.mkdir(new_path)
            recursive_copier(full_path, new_path)
