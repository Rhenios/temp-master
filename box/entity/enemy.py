import pygame
import random
import config
from config import width, height, enemy_bullet_speed
from box.entity.Bullet import Bullet
D = 30


class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy,armer=config.enemylevel):
        super().__init__()
        self.vx, self.vy = (vx, vy)
        self.type = .5+.5*int(random.random()*3)
        self.image = pygame.Surface((D*self.type, D*self.type))
        self.image.fill((255,255,255))
        self.rect = pygame.Rect(x, y, D*self.type, D*self.type)
        self.MAXHP = int((armer*2+2*random.random())*self.type)
        self.armer = int(self.MAXHP)
        self.x = x
        self.y = y
        self.CDR = int(random.random()*30)+20
        self.counta = 0
        self.level = armer
        self.speed = config.enemy_speed*1.5/(self.type)

    def update(self,e,x,y):
        if not (D < self.x < width - D-self.vx):
            self.vx *= -1
        if not (D < self.y < height - D-self.vy):
            self.vy *= -1
        self.rect.move_ip(self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy
        self.shoot(x,y,e)

    def hit(self,e,h):
        self.armer -= 1
        if self.armer<=0:
            try:
                e.remove(h)
                return config.base_exp * self.level
            except:
                pass
        elif self.armer <= self.MAXHP//3:
            self.image.fill((255,0,0))
        elif self.armer <= self.MAXHP*2//3:
            self.image.fill((255,255,0))
        return 0

    def shoot(self,x,y,bullet):
        if self.CDR < int(self.counta*self.type):
            X = x - self.x
            Y = y - self.y
            time = (X ** 2 + Y ** 2)**.5 / enemy_bullet_speed
            bullet.add(Bullet(self.x,self.y+D/2,X/time,Y/time,(255,0,0)))
            self.CDR = int(random.random()*30)+100
            self.ChangeSpeed()
            self.counta = 0
        else:
            self.counta += 1

    def ChangeSpeed(self):
        self.vx,self.vy = int(random.random() * self.speed - self.speed / 2), int(random.random() * self.speed - self.speed / 2)
