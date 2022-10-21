# TODO create queries folder (child of src) where this file will be
import main

dataframes = main.generate_dataframes()

# No diretorio raiz rodar: python3 src/extract/classes_by_ra_query.py
# Teste de query que pega as disciplinas deferidas apos ajuste do João Oliveira
print(dataframes[1].columns)
print(dataframes[1].loc[dataframes[1]['RA'] == 11202020252]['TURMA2'].tolist())
