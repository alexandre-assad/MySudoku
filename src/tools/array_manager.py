from src.generator.grid import *
from src.generator.case import *

def get_grid_list(liste:list):
    
    matrix = []
    under_list= []
    for i in range(81):
        if i % 9 == 0 and i != 0:
            matrix.append(under_list)
            under_list = []
        under_list.append(Case(liste[i],i//9,i%9))
    matrix.append(under_list)
    print(matrix)
    return Grid(matrix)