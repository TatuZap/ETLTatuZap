import get_files
import extrator

def get_all_dataframes():
    # Dataframes
    dfs = []

    # Generates all dataframes from files list
    for file in get_files.files():
        dfs.append(extrator.extrator(file,'AJUSTE_2022.3'))
    return dfs
