import numpy as np



""" 
Input : two lists
Output : One list, which is the intersection of the two input's lists
"""
def inter(arr1:list,arr2:list) -> list:
    return np.intersect1d(arr1,arr2)


""" 
Input : two lists
Output : One list, which is the opposite of the intersection of the two input's lists
"""
def exter(arr1:list,arr2:list) -> list:
    
    dif1 = np.setdiff1d(arr1, arr2)
    dif2 = np.setdiff1d(arr2, arr1)
    temp3 = np.concatenate((dif1, dif2))
    return temp3


"""
To be continued
def is_unique(value:int,arr:list) -> bool:
    return 
"""