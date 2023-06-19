from src.layout.game import *
from src.utils.random_manager import *


def backtracking_grid(grid):
    """
    Input : A grid 
    Basic code : For each case, if there is only one potential value it will put it in the case
    If there is not only one, it will go in recursive with one potential value, with a second function that return a boolean
    Output : the grid
    """
    
    true_basic_grid = grid
    print('Done')
    print('----------')
    print(true_basic_grid)
    print('----------')
    #Compléter l'évidence
    grid = complete_values_simple(grid)
        
    if grid.first_empty_case() != True:
        
        #Recursive de la première case vide
        index_value = grid.first_empty_case()
        list_value = grid.g_matrix[index_value[0]][index_value[1]].potential_value
        list_value = shuffle_list(list_value)
        for i in range(len(list_value)):
            print(true_basic_grid)
            n_grid = grid
            n_grid.g_matrix[index_value[0]][index_value[1]].value = list_value[i]
            #print(n_grid)
            if backtracking_bool(n_grid):
                print("true",i)
                print('Backtracking...')
                return backtracking_grid(n_grid)
            
    #Si grille juste return la grille
    else:
        return true_basic_grid



def backtracking_bool(grid):
    """
    Input : a grid
    Basic code : It is the recursive function, that will say true with the right value for a case
    Output : a boolean, true if it is the right number recursive
    """
    
    basics_grid = grid
    if grid.is_grid_correct():
        return True
    #Compléter l'évidence
    elif complete_values_simple(grid) == False:
        grid = basics_grid
        return False
    grid = complete_values_simple(grid)
                
    if grid.first_empty_case() != True:
               
         #Recursive de la première case vide 
        index_value = grid.first_empty_case()
        list_value = grid.g_matrix[index_value[0]][index_value[1]].potential_value
        list_value = shuffle_list(list_value)
        
        
        
        for i in range(len(list_value)):
            n_grid =grid
            
            n_grid.g_matrix[index_value[0]][index_value[1]].value = list_value[i]
   
            if backtracking_bool(n_grid):
                return backtracking_bool(n_grid)
        
    

def complete_values_simple(grid):
    """
    Input : a grid 
    Output : either false if there is a problem, or the grid completed with easy values
    """
    array_potential = []
    for i in range(9):
        for j in range(9):
            
            if grid.g_matrix[i][j].value == "_":
                
                for number in range(1,10):
                    
                    if grid.is_case_numbered(i,j,number):
                        
                        array_potential.append(number)
                  
                #Si grille fausse return False      
                if array_potential == []:
                    return False
                
                if grid.g_matrix[i][j].get_value(array_potential):
                    
                    return complete_values_simple(grid)
                array_potential = [] 
    return grid
