import pygame
from config import D

class Object(pygame.sprite.Sprite):

    def __init__(self,x,y,level,DD = D):
        super().__init__()
        self.armer = 100000000000
        self.image = pygame.Surface((DD, DD))
        self.image.fill((100,100,100))
        self.rect = pygame.Rect(x, y, DD, DD)
        self.level = level

    def hit(self,e,h):
        self.armer -= 1
        if self.armer<=0:
            try:
                e.remove(h)
            except:
                pass
        elif self.armer == 2:
            self.image.fill((255,255,0))
        elif self.armer == 1:
            self.image.fill((255,0,0))