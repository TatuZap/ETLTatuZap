import unidecode
import pandas as pd
import json
import main

def tratamento_matriculas_pos_ajuste(df):
    df.rename(columns={df.columns[0]: 'new'},inplace=True)
    df['new'] = df['new'].str.strip()
    df[['RA', 'CODIGO_TURMA', 'REMOVER','REMOVER','TURMA']] = df['new'].str.split(" ",4, expand=True)

    df1 = df.loc[df['RA'].str.len() == 11]
    df2 = df.loc[df['RA'].str.len() > 11]
    
    def spliter(item):return unidecode.unidecode(item)
    df2[['RA', 'CODIGO_TURMA', 'REMOVER','REMOVER','TURMA']] = df2['RA'].apply(spliter).str.split(" ",4, expand=True)
    df = pd.concat([df1,df2])
    df.drop(columns=['new', 'REMOVER'],inplace=True)
    df['TURMA'] = df['TURMA'].str.strip()

    return df


def tratamento_turmas_ingressantes(df):
    def add_space(item): 
        if len(str(item))<12 : return str(item) + '  '
        return str(item)
    df.iloc[:,0] = df.iloc[:,0].apply(add_space)
    df['temp'] = df.iloc[:,0].astype(str) + df.iloc[:,1].astype(str) + df.iloc[:,2].astype(str)
    df['temp'] = df['temp'].str.replace('nan','')
    df.drop(df.columns[[0,1,2]],axis=1,inplace=True)
    df[['RA','CURSO']] = df.iloc[:,6].str.split(" ",1,expand=True)
    df.drop(df.columns[[6]],axis=1,inplace=True)
    df['temp'] = df.iloc[:,3].astype(str) + df.iloc[:,4].astype(str)
    df['temp'] = df['temp'].str.replace('nan','')
    df.drop(df.columns[[3,4]],axis=1,inplace=True)
    df.rename(columns={"temp": "TURNO"},inplace=True)
    return df

def tratamento_ajuste(df):
    labels = df.loc[0].values.tolist()
    labels[5] = 'Codigo Disciplina'
    labels[6] = 'turma_cod'
    labels[20] = 'VAGAS REMANESCENTES'
    df.columns = labels
    df.drop([0],inplace=True)
    return df

def list_df_to_json(dfs):
    list = []
    for df in dfs:
        list.append(json.loads(df.to_json(orient="table",index=False))['data'])
    return list

def tratamento():
    dfs = main.get_all_dataframes()
    dfs[0] = tratamento_ajuste(dfs[0])
    dfs[1] = tratamento_matriculas_pos_ajuste(dfs[1])
    dfs[3] = tratamento_turmas_ingressantes(dfs[3])
    return list_df_to_json(dfs)
   

dfs = tratamento()
