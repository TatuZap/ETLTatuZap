import os

path=os.path.realpath('../files')
folder = os.path.dirname(path)
files=os.listdir(folder)

print(files)