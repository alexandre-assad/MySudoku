from src.layout.game import *
from src.generator.grid import *
from src.generator.case import *
from src.utils.txt_manager import *
from src.utils.os_manager import *



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

sudoku_map = generate_map_from_txt("sudoku1.txt")
    

"""
To be ereased, first test of sudoku matrix
"""



"""
Input : str, state of the current game
Basic Code : While loops, where it loops the scene (game, home, etc...)
Outpout : the pygame scene
"""

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