import pygame

def one_key(event):

    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_UP:
            return True
        return False