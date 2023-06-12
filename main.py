from src.layout.game import *
from src.generator.grid import *
from src.generator.case import *
from src.utils.txt_manager import *
from src.utils.os_manager import *





sudoku_map = generate_map_from_txt("sudoku1.txt")
print(sudoku_map)

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