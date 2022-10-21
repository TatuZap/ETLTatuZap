import get_files
import extrator

dfs = []
for file in get_files.files():
    dfs.append(extrator.extrator(file,'AJUSTE_2022.3'))

dfs[1].rename(columns={dfs[1].columns[0]: 'new'},inplace=True)
dfs[1]['new'] = dfs[1]['new'].str.strip()
dfs[1][['RA', 'CODIGO_TURMA', 'REMOVER','REMOVER','TURMA']] = dfs[1]['new'].str.split(" ",4, expand=True)

