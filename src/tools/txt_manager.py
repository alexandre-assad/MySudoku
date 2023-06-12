from src.utils.os_manager import *
from src.generator.grid import *
from src.generator.case import *


"""
Input : a text file
Outpout : a 2d array with the grid of sudoku from the file
"""
def parse(file):
    with open (file) as f:
        content = f.read()
    content = "".join(content.splitlines())
    sudoku_array = []
    sub_sudoku_array = []
    for i in range(9):
        for j in range(9):
            sub_sudoku_array.append(content[i*9+j])
        sudoku_array.append(sub_sudoku_array)
        sub_sudoku_array = []
    return np.array(sudoku_array)


"""
Input : a text file
Outpout : create a Grid with Case which have value from the file
"""
def generate_map_from_txt(file):
    sudoku_list = parse(sudoku_path(file))
    final_sudoku_map = []
    sub_sudoku_map = []
    for i in range(9):
        for j in range(9):
            sub_sudoku_map.append(Case(value=sudoku_list[i][j],x=i,y=j))
        final_sudoku_map.append(sub_sudoku_map)
        sub_sudoku_map = []
    sudoku_map = Grid(final_sudoku_map)
    return sudoku_map