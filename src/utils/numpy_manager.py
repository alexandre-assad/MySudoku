import numpy 



""" 
Input : two lists
Output : One list, which is the intersection of the two input's lists
"""
def inter(arr1:list,arr2:list) -> list:
    return numpy.intersect1d(arr1,arr2)