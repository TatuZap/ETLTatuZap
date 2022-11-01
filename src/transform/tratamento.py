from .matriculas_pos_ajuste import tratamento_matriculas_pos_ajuste as tratamento_matriculas_pos_ajuste
from .turmas_ingressantes import tratamento_turmas_ingressantes as tratamento_turmas_ingressantes
from .ajuste import tratamento_ajuste as tratamento_ajuste
import json

def list_df_to_json(dfs):
    list = []
    for df in dfs:
        list.append(json.loads(df.to_json(orient="table",index=False))['data'])
    return list

def to_json_file(dfs):
    i=0
    for df in dfs:
        i = i + 1
        df.df.to_json(path_or_buf='C:\\Users\\Danilo\\Documents\\UFABC\LABES\\ETLTatuZap\\src\\output\\data'+str(i)+'.json',orient="table",index=False)
    return list


def tratamento_json(get_all_dataframes):
    dfs = get_all_dataframes()
    dfs[0]["df"]= tratamento_ajuste(dfs[0]["df"])
    dfs[1]["df"]= tratamento_matriculas_pos_ajuste(dfs[1]["df"])
    dfs[3]["df"] = tratamento_turmas_ingressantes(dfs[3]["df"])
    return list_df_to_json(dfs)

def tratamento_df(get_all_dataframes):
    dfs = get_all_dataframes()
    dfs[0]["df"] = tratamento_ajuste(dfs[0]["df"])
    dfs[1]["df"] = tratamento_matriculas_pos_ajuste(dfs[1]["df"])
    dfs[3]["df"]= tratamento_turmas_ingressantes(dfs[3]["df"])
    return dfs


