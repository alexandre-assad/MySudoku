import pygame

class Button:
    def __init__(self,x:int,y:int,image,func=None):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft= (x,y)
        self.clicked = False
        self.func = func
        
    def draw(self,game):
        """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    if self.clicked == False:
                        print("hey")
                        self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        """
        game.screen.blit(self.image,(self.rect.x,self.rect.y))