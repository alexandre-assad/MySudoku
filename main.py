from src.layout.game import *


def main():
    game_object = create_display_game()
    while state == "game":
        events = pygame.event.get()
        state = display_game(sokoban_map,game_object,first_player)
        for event in events:
            if event.type == pygame.QUIT:
                state = "over"
                
            sokoban_map = game_event(event,first_player,sokoban_map)

    pygame.quit()

if __name__ == "__main__":
    main()