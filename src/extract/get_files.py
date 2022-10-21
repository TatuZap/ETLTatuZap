import os
import pandas as pd

# Determines the file separator depending on OS ('\\' for Windows and '/' for Linux)
directory_separator = '\\' if os.name == 'nt' else '/'

# Determines the path to the files directory
current_path = os.path.dirname(os.path.abspath(__file__))
head, sep, tail = current_path.partition('ETLTatuZap')
files_path = head + sep + directory_separator + 'src' + directory_separator + 'files'

def files():
    path = os.path.realpath(files_path)
    files_name = os.listdir(path)
    files = []
    for file in files_name: files.append(path + directory_separator + file)
    return files
