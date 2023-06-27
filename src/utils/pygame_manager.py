import pygame



def one_key(event:pygame.event):
    """
    Input : An event
    Outpout : a boolean, True if the specific key has been pressed
    """

    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_1:
            return True
        return False