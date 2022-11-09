# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 01:07:48 2022

@author: Danilo
"""
import json
import pandas as pd

#pos ajuste
file = 'C:\\Users\\Danilo\\Documents\\UFABC\\LABES\\ETLTatuZap\\src\\transform\\turmas\\output\\matriculas_deferidas_pos_ajuste_2022.3.xlsx.json'
pos_ajuste_file = open(file)
pos_ajuste_json = json.load(pos_ajuste_file)['data']
pos_ajuste_str = json.dumps(pos_ajuste_json)

