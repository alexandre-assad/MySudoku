import numpy as np



def inter(arr1:list,arr2:list) -> list:
    """ 
    Input : two lists
    Output : One list, which is the intersection of the two input's lists
    """
    return np.intersect1d(arr1,arr2)


def exter(arr1:list,arr2:list) -> list:
    """ 
    Input : two lists
    Output : One list, which is the opposite of the intersection of the two input's lists
    """
    
    dif1 = np.setdiff1d(arr1, arr2)
    dif2 = np.setdiff1d(arr2, arr1)
    temp3 = np.concatenate((dif1, dif2))
    return temp3




def is_unique(value:int,arr:list) -> bool:
    """
    Input : an int and an array
    Basic code : True if the int is unique in the array
    Output : A boolean
    """
    if value in arr:
        return False
    else:
        return True


