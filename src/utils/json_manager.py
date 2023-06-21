import json
from src.utils.os_manager import *

def dump_json_sudoku(liste : list):
    new_list = []
    for i in range(len(liste)):
        for j in range(len(liste[0])):
            new_list.append(liste[i][j].value)
            
            
    data = {"sudoku_grid":new_list}
    with open(solve_sudoku_path(), 'w') as f:
        json.dump(data, f, indent=4)

def load_json_sudoku():
    with open(solve_sudoku_path(), 'r') as f:
        dico = json.loads(f.read())
    list = dico["sudoku_grid"]
    return list
    