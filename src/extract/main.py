import get_files
import extrator

dfs = []
for file in get_files.files():
    dfs.append(extrator.extrator(file,'AJUSTE_2022.3'))

print(dfs)