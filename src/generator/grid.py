from src.utils.numpy_manager import *

class Grid:
    
    
    def __init__(self,grid_matrix:list):
        self.g_matrix = grid_matrix
        
        
    def __str__(self):
        for row in self.g_matrix:
            print(row)
        return ""
    
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
                if x!= i or y!= j:
                    list_values.append(self.g_matrix[box[0]*3+i][box[1]*3+j].value)
        for i in range(len(list_values)):
            if list_values[i] == "_":
                list_values[i] = 0
            else:
                list_values[i] = int(list_values[i])
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
            if i != x:
                list_values_1.append(self.g_matrix[i][y].value)
                
        for j in range(9):
            if j != y:
                list_values_2.append(self.g_matrix[x][j].value)
            
        #I Rewrite good lists
        for i in range(len(list_values_1)):
            if list_values_1[i] == "_":
                list_values_1[i] = 0
            else:
                list_values_1[i] = int(list_values_1[i])
                
            if list_values_2[i] == "_":
                list_values_2[i] = 0
            else:
                list_values_2[i] = int(list_values_2[i])
            
        list_value = np.array([list_values_1,list_values_2])
        list_value = np.unique(list_value)
        
        return exter(list_value,[1,2,3,4,5,6,7,8,9])
    
    '''
    Input : the grid
    Outpout : True if it's not finished, false if it is
    '''
    def not_win(self):
        for i in range(9):
            for j in range(9):
                if str(self.potential_value_box(i,j)[0]) == self.g_matrix[i][j].value and str(self.potential_value_box(i,j)[0]) == self.g_matrix[i][j].value:
                    pass
                else:
                    return True
        return False
    
    
    """
    Now i will create other function to developp an other way to solve the sudoku
    I will create a way more "human" to solve it
    """
    
    """
    Input : coordinates and a number to Test
    Output : True if it can have the potential value of the number, else False
    """
    def is_case_numbered(self,x,y,number):
        box = self.potential_value_box(x,y)
        lines = self.potential_value_lines(x,y)
        return number in box and number in lines
            