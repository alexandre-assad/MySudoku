import random


def shuffle_list(arr:list):
    """
    Input : an array
    Output : an array, shuffle
    """
    random.shuffle(arr)
    return arr

def random_int(start,end):
    return random.randint(start,end)