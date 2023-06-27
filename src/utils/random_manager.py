import random


def shuffle_list(arr:list):
    """
    Input : an array
    Output : an array, shuffle
    """
    random.shuffle(arr)
    return arr

def random_int(start:int,end:int):
    """
    Input : 2 int
    Output : A random int in the range of the two int
    """
    return random.randint(start,end)