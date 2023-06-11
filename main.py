from src.layout.game import *
from src.generator.grid import *
from src.generator.case import *

sudoku_list = []
sub_sudoku = []
for i in range(9):
    for j in range(9):
        sub_sudoku.append(Case(2,i,j))
    sudoku_list.append(sub_sudoku)
    sub_sudoku = []
print(sudoku_list)
sudoku_map = Grid(sudoku_list)
sudoku_map.g_matrix[2][4]= Case(5,2,4)

def main(state):
    game_object = create_display_game()
    while state == "game":
        events = pygame.event.get()
        state = display_game(game_object,sudoku_map)
        for event in events:
            if event.type == pygame.QUIT:
                state = "over"
                
            #sokoban_map = game_event(event,first_player,sokoban_map)

    pygame.quit()

if __name__ == "__main__":
    main("game")