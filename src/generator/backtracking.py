from src.layout.game import *
from src.utils.random_manager import *
from src.utils.json_manager import *
from src.tools.array_manager import *

def simple_backtracking(grid):
    for i in range(9):
        for j in range(9):
            if grid.g_matrix[i][j].value == 0:
                for number in range(1,10):
                    if grid.is_case_numbered(i,j,number):
                        grid.g_matrix[i][j].value = number
                        simple_backtracking(grid)
                        grid.g_matrix[i][j].value = 0
                return False
    dump_json_sudoku(grid.g_matrix)
    print(grid)
