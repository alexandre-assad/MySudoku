import pygame


"""
For all the fuctions :
Input : An event
Outpout : a boolean, True if the specific key has been pressed
"""

def one_key(event):

    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_1:
            return True
        return False