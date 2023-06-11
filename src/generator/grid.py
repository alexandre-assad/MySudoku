from src.utils.numpy_manager import *

class Grid:
    
    
    def __init__(self,grid_matrix:list):
        self.g_matrix = grid_matrix
        
        
    def __str__(self):
        for i in self.g_matrix:
            print(i)
    
    """
    Input : two int and a matrix, coordinates x and y of a case, with the matrix of the grid
    Basic structure : Find the 3x3 box where the case is, and test all the available values left
    Outpout : a list, All the potential value the case could have in the box (3x3)
    """
    def potential_value_box(self,x,y):
        list_values = []
        box = [x//3,y//3]
        for i in range(3):
            for j in range(3):
                list_values.append(self.g_matrix[box[0]*3+i][box[1]*3+j])
        return exter(list_values,[1,2,3,4,5,6,7,8,9])
    
    """
    Input : two int and a matrix, coordinates x and y of a case, with the matrix of the grid
    Basic code : Test all the available values for each axis
    Outpout : a list, All the potential value the case could have in the two axis (y-axis and x-axis)
    """
    def potential_value_lines(self,x,y):
        list_values_1 = []
        list_values_2 = []
        for i in range(9):
            list_values_1.append(self.g_matrix[i][y])
        for j in range(9):
            list_values_2.append(self.g_matrix[x][j])
        return exter(exter(list_values_1,[1,2,3,4,5,6,7,8,9]),list_values_2)
    
test_grid = Grid([[1,2,3],[5,8,9],[2,4,7],[3,6,1,2],[7,9],[1],[4,5],[6,8],[2,4]])
print(test_grid.potential_value_lines(3,7))