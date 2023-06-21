from src.utils.json_manager import *

def force_brute(grid):
    global basic_grid
    for i in range(9):
        for j in range(9):
            if grid.g_matrix[i][j].value == 0:
                for number in range(1,10):
                    if grid.is_case_numbered(i,j,number):
                        grid.g_matrix[i][j].value = number
                        force_brute(grid)
                        grid.g_matrix[i][j].value = 0
                return False
    dump_json_sudoku(grid.g_matrix)
    print(grid)