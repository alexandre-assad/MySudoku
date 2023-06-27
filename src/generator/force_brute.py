from src.utils.random_manager import *
from src.utils.numpy_manager import *
from src.generator.grid import *
from src.generator.case import *

def simple_brute_force(grid:Grid):
    """
    Input : A grid
    Basic code : For each empty case, get a random_int, test if the grid it's correct, then try again
    Output : A completed grid
    """
    
    list_index_empty_case = grid.all_empty_cases()
    while grid.is_grid_correct() != True or grid.first_empty_case() != True:
        for i in range(len(list_index_empty_case)):
            grid.g_matrix[list_index_empty_case[i][0]][list_index_empty_case[i][1]].value = 0
        for i in range(len(list_index_empty_case)):
            grid.g_matrix[list_index_empty_case[i][0]][list_index_empty_case[i][1]].value = random_int(1,9)
    return grid


def advance_brute_force(grid:Grid):
    """
    Input : A grid
    Basic code : Test if there are obvious value, then try random value in the potential values of each empty case, do it till it's tru
    Output : a completed grid
    """
    
    list_index_empty_case = grid.all_empty_cases()
    grid.get_potential()
    while grid.is_grid_correct() != True or grid.first_empty_case() != True:
        
        for i in range(len(list_index_empty_case)):
            grid.g_matrix[list_index_empty_case[i][0]][list_index_empty_case[i][1]].value = 0
        for i in range(len(list_index_empty_case)):
            
            potential_value =  grid.g_matrix[list_index_empty_case[i][0]][list_index_empty_case[i][1]].potential_value
            grid.g_matrix[list_index_empty_case[i][0]][list_index_empty_case[i][1]].value = potential_value[random_int(0,len(potential_value)-1)]
            
    return grid