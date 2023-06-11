import pygame 
from src.generator.game_class import Game
from src.utils.os_manager import *

def position_in_grid(y,x):
    return [y*71,x*71]

def create_display_game():
    global oneImg,twoImg,threeImg,fourImg,fiveImg,sixImg,sevenImg,eightImg,nineImg,backgroundImg
    pygame.init()
    game_object = Game(screen=pygame.display.set_mode((800,600)),size=[(800,600)])
    pygame.display.set_caption("My Sokoban")
    oneImg = pygame.image.load(sprite_path("number_one.png")).convert_alpha()
    twoImg = pygame.image.load(sprite_path("number_two.png")).convert_alpha()
    threeImg = pygame.image.load(sprite_path("number_three.png")).convert_alpha()
    fourImg = pygame.image.load(sprite_path("number_four.png")).convert_alpha()
    fiveImg = pygame.image.load(sprite_path("number_five.png")).convert_alpha()
    sixImg = pygame.image.load(sprite_path("number_six.png")).convert_alpha()
    sevenImg = pygame.image.load(sprite_path("number_seven.png")).convert_alpha()
    eightImg = pygame.image.load(sprite_path("number_eight.png")).convert_alpha()
    nineImg = pygame.image.load(sprite_path("number_nine.png")).convert_alpha()
    backgroundImg = pygame.image.load(sprite_path("background_sudoku.png")).convert_alpha()
    return game_object


def display_game(game,grid):
    game.screen.blit(backgroundImg,(0,0))
    for i in range(9):
        for j in range(9):
            if grid.g_matrix[i][j].value == 1:
                game.screen.blit(oneImg,position_in_grid(i,j))
            elif grid.g_matrix[i][j].value == 2:
                game.screen.blit(twoImg,position_in_grid(i,j))
            elif grid.g_matrix[i][j].value == 3:
                game.screen.blit(threeImg,position_in_grid(i,j))
            elif grid.g_matrix[i][j].value == 4:
                game.screen.blit(fourImg,position_in_grid(i,j))
            elif grid.g_matrix[i][j].value == 5:
                game.screen.blit(fiveImg,position_in_grid(i,j))
            elif grid.g_matrix[i][j].value == 6:
                game.screen.blit(sixImg,position_in_grid(i,j))
            elif grid.g_matrix[i][j].value == 7:
                game.screen.blit(sevenImg,position_in_grid(i,j))
            elif grid.g_matrix[i][j].value == 8:
                game.screen.blit(eightImg,position_in_grid(i,j))
            elif grid.g_matrix[i][j].value == 9:
                game.screen.blit(nineImg,position_in_grid(i,j))
    pygame.display.update()
    return "game"