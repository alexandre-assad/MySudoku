from src.layout.game import *
from src.utils.random_manager import *
from src.tools.constant import *


def backtracking(grid):
    if grid.is_grid_correct() == False:
        return False
    elif grid.first_empty_case() == True:
        if grid.is_grid_correct():
            return grid
        
    grid = complete_values_simple(grid)
    basic_grid = grid
    
    for potential_value in grid.g_matrix[grid.first_empty_case()[0]][grid.first_empty_case()[1]].potential_value:
        print(basic_grid)
        grid.g_matrix[grid.first_empty_case()[0]][grid.first_empty_case()[1]].value = potential_value
        
        
        if backtracking(grid) != False:
            return backtracking(grid)
        
        grid = basic_grid
    
    
    
def complete_values_simple(grid):
    """
    Input : a grid 
    Basic code : for each box 3x3, see if there is a number that could only be place at one case
    Output : either false if there is a problem, or the grid completed with easy values
    """
    while True:
        for number in range(1,10):
            
            for x_box in range (3):
                
                for y_box in range (3):
                    
                    if is_number_alone(number,x_box,y_box,grid) != False:
                        
                        grid.g_matrix[is_number_alone(number,x_box,y_box,grid)[0]][is_number_alone(number,x_box,y_box,grid)[1]].value = number
                        return complete_values_simple(grid)
        grid.get_potential()
        return grid
    
                        
def is_number_alone(number, x_box,y_box,grid):
    """
    Input : a number, numbers of the box(x and y), and a grid
    Output : False if the number could not be place easily in the box, or the coordinates if it can
    """
    compteur = 0
    
    position = [0,0]
    
    for i in range(3):
        
        for j in range(3):
            
            if grid.g_matrix[x_box*3+i][y_box*3+j].value == 0:
                
                if grid.is_case_numbered(x_box*3+i,y_box*3+j,number):
                     
                    
                    compteur +=1
                    position = [x_box*3+i,y_box*3+j]
                    
                    #if x_box == 2 and y_box==2:
                        #print("Last Case",i,j,position)
                    
    if compteur == 1:
        
        return position
    
    else:
        
        return False