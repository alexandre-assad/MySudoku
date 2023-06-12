from src.utils.os_manager import *
from src.generator.grid import *
from src.generator.case import *

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
    return sudoku_array


def generate_map_from_txt(file):
    sudoku_list = parse(sudoku_path(file))
    final_sudoku_map = []
    sub_sudoku_map = []
    for i in range(9):
        for j in range(9):
            sub_sudoku_map.append(Case(value=sudoku_list[j][i],x=i,y=j))
        final_sudoku_map.append(sub_sudoku_map)
        sub_sudoku_map = []
    sudoku_map = Grid(final_sudoku_map)
    return sudoku_map