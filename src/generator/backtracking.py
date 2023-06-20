from src.layout.game import *
from src.utils.random_manager import *
from src.tools.constant import *

def complete_values_simple(grid):
    """
    Input : a grid 
    Output : either false if there is a problem, or the grid completed with easy values
    """
    while True:
        
        for number in range(1,10):
            
            for x_box in range (3):
                
                for y_box in range (3):
                    
                    if is_number_alone(number,x_box,y_box,grid) != False:
                        
                        grid.g_matrix[is_number_alone(number,x_box,y_box,grid)[0]][is_number_alone(number,x_box,y_box,grid)[1]].value = number
                        number = 0
            if number == 9:
                return grid
    
                        
def is_number_alone(number, x_box,y_box,grid):
    
    compteur = 0
    
    position = [0,0]
    
    for i in range(3):
        
        for j in range(3):
            
            if grid.g_matrix[x_box*3+i][y_box*3+j].value == "_":
                
                if grid.is_case_numbered(x_box*3+i,y_box*3+j,number):
                    
                    compteur +=1
                    position = [x_box*3+i,y_box*3+j]
                    
    if compteur == 1:
        
        return position
    
    else:
        
        return False