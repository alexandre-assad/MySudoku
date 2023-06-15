from src.layout.game import *
from src.utils.random_manager import *

"""
Input : A grid 
Basic code : For each case, if there is only one potential value it will put it in the case
If there is not only one, it will go in recursive with one potential value, with a second function that return a boolean
Output : the grid
"""
def backtracking(grid):
    
    array_potential = []
    for i in range(9):
        for j in range(9):
            
            if grid.g_matrix[i][j].value == "_":
                
                for number in range(1,10):
                    if grid.is_case_numbered(i,j,number):
                        array_potential.append(number)
                if array_potential == []:
                    return False
                if grid.g_matrix[i][j].get_value(array_potential):
                    backtracking(grid)
                array_potential = [] 
                
        if grid.first_empty_case() != True:
            
            index_value = grid.first_empty_case()
            list_value = grid.g_matrix[index_value[0]][index_value[1]].potential_value
            list_value = shuffle_list(list_value)
            n_grid =grid
            for i in range(len(list_value)):
                n_grid.g_matrix[index_value[0]][index_value[1]].value = list_value[i]
                if backtracking_2(n_grid) == True :
                    grid = n_grid
        else:
            return grid

"""
Input : a grid
Basic code : It is the recursive function, that will say true with the right value for a case
Output : a boolean, true if it is the right number recursive
"""
def backtracking_2(grid):
    
    array_potential = []
    for i in range(9):
        for j in range(9):
            
            if grid.g_matrix[i][j].value == "_":
                
                for number in range(1,10):
                    if grid.is_case_numbered(i,j,number):
                        array_potential.append(number)
                if array_potential == []:
                    return False
                if grid.g_matrix[i][j].get_value(array_potential):

                    backtracking_2(grid)
                array_potential = [] 
                
    if grid.first_empty_case() != True:
                
        index_value = grid.first_empty_case()
        list_value = grid.g_matrix[index_value[0]][index_value[1]].potential_value
        list_value = shuffle_list(list_value)
        n_grid =grid
        for i in range(len(list_value)):
            n_grid.g_matrix[index_value[0]][index_value[1]].value = list_value[i]
            return backtracking_2(n_grid)
    else:
        return True
