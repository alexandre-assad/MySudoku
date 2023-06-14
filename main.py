from src.layout.game import *
from src.generator.grid import *
from src.generator.case import *
from src.tools.txt_manager import *
from src.utils.os_manager import *
from src.generator.backtracking import *




sudoku_map = generate_map_from_txt("sudoku1.txt")
print(sudoku_map)
print(sudoku_map.not_win())


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
        print(backtracking(sudoku_map))


    pygame.quit()

if __name__ == "__main__":
    main("game")