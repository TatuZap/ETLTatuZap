import os
import pandas as pd

def files():
    path=os.path.realpath('./src/files')
    files_name=os.listdir(path)
    files = []
    for file in files_name: files.append(path + '\\' +file)
    return files

