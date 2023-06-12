

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
