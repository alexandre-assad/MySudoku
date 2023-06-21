from src.layout.game import *
from src.generator.grid import *
from src.generator.case import *
from src.tools.txt_manager import *
from src.utils.os_manager import *
from src.generator.backtracking import *
from src.generator.force_brute import *


current_map = generate_map_from_txt("sudoku2.txt")
print(current_map)
print(force_brute(current_map))
load_json_sudoku()
print(current_map.is_grid_correct())



"""
Input : str, state of the current game
Basic Code : While loops, where it loops the scene (game, home, etc...)
Outpout : the pygame scene
"""

def main(state,current_map):
    
    
    game_object = create_display_game()
    while state == "game":
        events = pygame.event.get()
        state = display_game(game_object,current_map)
        for event in events:
            if event.type == pygame.QUIT:
                state = "over"
        
        #print(current_map)

    pygame.quit()

if __name__ == "__main__":
    main("game",current_map)