import pygame 
from src.generator.game_class import Game
from src.utils.os_manager import *
from src.generator.button import *

"""
Input : coordinates x and y in a matrix
Outpout : an array of coordinates in a pygame scene
"""
def position_in_grid(y,x):
    return [y*71,x*71]


"""
Outpout : Create and init all the display of the Pygame scene (images, game_object,etc...)
"""

def create_display_game():
    global emptyImg, oneImg,twoImg,threeImg,fourImg,fiveImg,sixImg,sevenImg,eightImg,nineImg,backgroundImg
    pygame.init()
    game_object = Game(screen=pygame.display.set_mode((800,630)),size=[(800,600)])
    pygame.display.set_caption("My Sokoban")
    emptyImg = pygame.image.load(sprite_path("number_empty.png")).convert_alpha()
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


"""
Input : A game object and a matrix
Basic Code : For each value of the matrix, create a button with the image of the number
Outpout : Display the screen of the game object, where there are images correlated to the matrix values
"""

def display_game(game,grid):
    game.screen.blit(backgroundImg,(0,0))
    
    for i in range(9):
        
        for j in range(9):
            
            if grid.g_matrix[i][j].value == 0:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=emptyImg)
                button.draw(game)
                
            elif grid.g_matrix[i][j].value == 1:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=oneImg)
                button.draw(game)
                
            elif grid.g_matrix[i][j].value == 2:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=twoImg)
                button.draw(game)
                
            elif grid.g_matrix[i][j].value == 3:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=threeImg)
                button.draw(game)
                
            elif grid.g_matrix[i][j].value == 4:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=fourImg)
                button.draw(game)
                
            elif grid.g_matrix[i][j].value == 5:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=fiveImg)
                button.draw(game)
                
            elif grid.g_matrix[i][j].value == 6:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=sixImg)
                button.draw(game)
                
            elif grid.g_matrix[i][j].value == 7:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=sevenImg)
                button.draw(game)
                
            elif grid.g_matrix[i][j].value == 8:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=eightImg)
                button.draw(game)
                
            elif grid.g_matrix[i][j].value == 9:
                button = Button(x=position_in_grid(i,j)[0],y=position_in_grid(i,j)[1],image=nineImg)
                button.draw(game)
                
    pygame.display.update()
    return "game"