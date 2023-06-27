from src.utils.numpy_manager import *

class Grid:
    
    
    def __init__(self,grid_matrix:list):
        self.g_matrix = grid_matrix
        self.format()
        
    def __str__(self):
        for row in self.g_matrix:
            print(row)
        return ""
    
    
    def format(self):
        for i in range(9):
            for j in range(9):
                if self.g_matrix[i][j].value == "_":
                    self.g_matrix[i][j].value = 0
                else:
                    self.g_matrix[i][j].value = int(self.g_matrix[i][j].value)
        
        
        
        
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
        return exter(list_values,[0,1,2,3,4,5,6,7,8,9])
    
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

        list_value = np.array([list_values_1,list_values_2])
        list_value = np.unique(list_value)
        
        return exter(list_value,[0,1,2,3,4,5,6,7,8,9])
    
    def potential_value_row(self,row):
        list_value = []
        for i in range(9):
            list_value.append(self.g_matrix[row][i].value)
        return exter(list_value,[0,1,2,3,4,5,6,7,8,9])
        
    def not_win(self):
        '''
        Input : the grid
        Outpout : True if it's not finished, false if it is
        '''
        for i in range(9):
            for j in range(9):
                if self.g_matrix[i][j].value == 0:
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
    def is_case_numbered(self,x:int,y:int,number:int):
        box = self.potential_value_box(x,y)
        lines = self.potential_value_lines(x,y)
        return number in box and number in lines
            
    
    """
    Input : the grid
    Output : an array of two int, the coordinates of the firls empty case
    """
    def first_empty_case(self):
        for i in range(9):
            for j in range(9):
                if self.g_matrix[i][j].value == 0:
                    return [i,j]
        return True
    
    
    """
    Input : the grid and two int x and y, coordinates
    Output : A boolean, true if the case is well placed in the box
    """
    
    def is_good_case_box(self,x,y):
        box = [x//3,y//3]
        for i in range(3):
            for j in range(3):
                if i != x and j != y:
                    if self.g_matrix[box[0]*3+i][box[1]*3+j].value == self.g_matrix[i][j].value:
                        return False
        return True
    
    
    """
    Input : the grid and two int x and y, coordinates
    Output : A boolean, true if the case is well placed in the box
    """
    
    def is_good_case_line(self,x,y):
        list_number = []
        for i in range(9):
            if self.g_matrix[i][y].value != 0:
                if self.g_matrix[i][y].value not in list_number:
                    list_number.append(self.g_matrix[i][y].value)
                else:
                    return False
        list_number = []
        for j in range(9):
            if self.g_matrix[x][j].value != 0:
                if self.g_matrix[x][j].value not in list_number:
                    list_number.append(self.g_matrix[x][j].value)
                else:
                    return False
        return True
    
    def is_grid_correct(self):
        """
        Input : the grid completed
        Output: A boolean, true if the grid is correct
        """
        for i in range(9):
            if self.is_good_case_line(i,i) != True:
                    return False
        return True
    
    def get_potential(self):
        for i in range(9):
            for j in range(9):
                if self.g_matrix[i][j].value == 0:
                    self.g_matrix[i][j].get_value(inter(self.potential_value_lines(i,j),self.potential_value_box(i,j)))
                    
    def all_empty_cases(self):
        list_index_all = []
        for i in range(9):
            for j in range(9):
                if self.g_matrix[i][j].value == 0:
                    list_index_all.append([i,j])
        return list_index_all