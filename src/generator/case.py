from src.utils.numpy_manager import *

class Case:
    
    def __init__(self,value:int,x:int,y:int):
        
        self.value = value
        self.x = x
        self.y = y
        self.potential_value = []
        
        
    def __repr__(self):
        
        return str(self.value)
    
    """
    Input : an array that will be self.potential_value 
    Outpout : Self.value if there is only one potential value
    """
    def get_value(self,arr_potential:list):

        self.potential_value = arr_potential
        
        if len(self.potential_value)==1:
            
            self.value = self.potential_value[0]
            return True
        
        return False
        