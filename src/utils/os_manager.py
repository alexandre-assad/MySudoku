from os import path


"""
Input : a sprite's file name
Output : a str, the path to get the image 
"""
def sprite_path(file:str):
    sprite_path = "assets/sprites"
    return path.join(sprite_path,file)

def sudoku_path(file:str):
    sprite_path = "assets/sudoku_grids"
    return path.join(sprite_path,file)

def solve_sudoku_path():
    return "config/solve_sudoku.json"