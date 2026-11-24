import os
import shutil
from pathlib import Path
from gencontent import generate_page



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for p in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, p)
        if os.path.isfile(full_path):
            dest_file_path = os.path.join(dest_dir_path, p)
            dest_file_path = Path(dest_file_path).with_suffix(".html")
            generate_page(full_path, template_path, dest_file_path)
        if os.path.isdir(full_path):
            new_path = os.path.join(dest_dir_path, p)
            os.mkdir(new_path)
            generate_pages_recursive(full_path, template_path, new_path)
