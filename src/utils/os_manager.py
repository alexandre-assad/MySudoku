from os import path


def sprite_path(file:str):
    """
    Input : a sprite's file name
    Output : a str, the path to get the image 
    """
    sprite_path = "assets/sprites"
    return path.join(sprite_path,file)

def sudoku_path(file:str):
    """
    Input : a sudoku's file name
    Output : a str, the path to get the image 
    """
    sprite_path = "assets/sudoku_grids"
    return path.join(sprite_path,file)

def solve_sudoku_path():
    """
    Output : the path to solve_sudoku.json
    """
    return "config/solve_sudoku.json"