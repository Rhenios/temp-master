import pygame
import config
from config import bullet_D as Bulletd
from config import damage as D_Damage

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,vx,vy,color,BulletD=Bulletd,damage = D_Damage):
        super().__init__()
        self.x = x
        self.y = y
        self.vx = vx
        self.image = pygame.Surface((Bulletd+4+BulletD,BulletD))
        self.image.fill(color)
        self.rect = pygame.Rect(x,y,Bulletd+4*BulletD,BulletD)
        self.vy = vy
        self.damage = damage
        self.out = False

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.move_ip(self.vx,self.vy)
        if not((0 < self.x < config.width) or (0 < self.y < config.height)):
            self.out = True
