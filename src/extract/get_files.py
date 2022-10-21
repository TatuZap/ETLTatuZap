import os
import pandas as pd

# Determines the file separator depending on OS ('\\' for Windows and '/' for Linux)
directory_separator = '\\' if os.name == 'nt' else '/'

def files():
    path=os.path.realpath('../files')
    files_name=os.listdir(path)
    files = []
    for file in files_name: files.append(path + directory_separator + file)
    return files
