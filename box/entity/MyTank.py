import pygame

import config
from box.entity.Bullet import Bullet
from config import bulletspeed
from config import Tank_D, Tankspeed, tankcool


class Tank(pygame.sprite.Sprite):
    vy: int

    def __init__(self, x, y, vx, vy, armer):
        super().__init__()
        self.vx = vx
        self.vy = vy
        self.image = pygame.Surface((Tank_D, Tank_D))
        self.image.fill((35, 255, 255))
        self.rect = pygame.Rect(x, y, Tank_D, Tank_D)
        self.speed = Tankspeed
        self.x = x
        self.y = y
        self.cool = 0
        self.level = 1
        self.armer = armer
        self.exp = 0

    def add_exp(self, exp):
        level_table = int(self.level ^ 2 / 3 + 5)
        self.exp += exp
        if exp > level_table:
            self.level += 1
            self.exp -= level_table

    def up(self):
        self.vy = -self.speed

    def down(self):
        self.vy = self.speed

    def right(self):
        self.vx = self.speed

    def left(self):
        self.vx = -self.speed

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy
        self.vx = 0
        self.vy = 0
        if self.cool <= 100:
            self.cool += 1
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.up()
        if pressed_keys[pygame.K_DOWN]:
            self.down()
        if pressed_keys[pygame.K_RIGHT]:
            self.right()
        if pressed_keys[pygame.K_LEFT]:
            self.left()

    def shoot(self, bullets):
        if self.cooldown():
            bullets.add(Bullet(self.x, self.y + Tank_D / 2 - config.bullet_D / 2, -bulletspeed, 0, (255, 255, 0),
                               config.damage))
            bullets.add(Bullet(self.x+5, self.y + Tank_D / 2 - config.bullet_D / 2, -bulletspeed, 1, (255, 255, 0), config.damage))
            bullets.add(Bullet(self.x+5, self.y + Tank_D / 2 - config.bullet_D / 2, -bulletspeed, -1, (255, 255, 0), config.damage))

    def BIGshoot(self, bullets):
        bullets.add(Bullet(self.x, self.y + Tank_D / 2, -bulletspeed, 0, (200, 200, 0), 10))

    def cooldown(self):
        if self.cool >= tankcool:
            self.cool = 0
            return True
        else:
            return False

    def hit(self, e, h, d=config.damage):
        self.armer -= d
        if self.armer <= 0:
            try:
                e.remove(h)
            except Exception as e:
                print(e)
            return False
        return True

    def location(self):
        return self.x, self.y

    def Changespeed(self, v):
        self.speed = v
