

class Grid:
    
    
    def __init__(self,grid_matrix:list):
        self.g_matrix = grid_matrix
        
        
    def __str__(self):
        for i in self.g_matrix:
            print(i)
    
    """
    Input : two int and a matrix, coordinates x and y of a case, with the matrix of the grid
    Outpout : a list, All the potential value the case could have in the box (3x3)
    """
    def potential_value_box(self,x,y):
        pass
    
    
    """
    Input : two int and a matrix, coordinates x and y of a case, with the matrix of the grid
    Outpout : a list, All the potential value the case could have in the two axis (y-axis and x-axis)
    """
    def potential_value_lines(self,x,y):
        pass