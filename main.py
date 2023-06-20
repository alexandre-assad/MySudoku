from src.layout.game import *
from src.generator.grid import *
from src.generator.case import *
from src.tools.txt_manager import *
from src.utils.os_manager import *
from src.generator.backtracking import *



current_map = complete_values_simple(generate_map_from_txt("sudoku1.txt"))
print(current_map)


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