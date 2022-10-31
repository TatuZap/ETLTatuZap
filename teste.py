# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 01:07:48 2022

@author: Danilo
"""
import json
import pandas as pd

#pos ajuste
file = 'C:\\Users\\Danilo\\Documents\\UFABC\\LABES\\ETLTatuZap\\src\\output\\data2.json'
pos_ajuste_file = open(file)
pos_ajuste_json = json.load(pos_ajuste_file)
pos_ajuste_str = json.dumps(pos_ajuste_json)

#ajuste
file = 'C:\\Users\\Danilo\\Documents\\UFABC\\LABES\\ETLTatuZap\\src\\output\\data3.json'
ajuste_file = open(file)
ajuste_json = json.load(ajuste_file)['data']

#pos ajuste to df

#pos_ajuste_df = pd.read_json(pos_ajuste_str)

