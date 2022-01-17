import random

import pygame
import config
from box.entity.MyTank import Tank
from box.entity.Object import Object


def run_field():
    fieldsheet =  Field()
    fieldsheet.field_animation()


class Field:
    def __init__(self):
        self.screen = pygame.display.set_mode((config.width, config.height))
        self.fps = config.gamespeed
        self.h = config.height
        self.w = config.width
        self.encounters = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.tank = pygame.sprite.Group()
        from Battle import Battle
        self.battle = Battle()
        for i in range(10):
            self.make_encounter(int(config.enemylevel - 3*random.random()))
        self.tank.add(Tank(1180, 360, 0, 0, 1))

    def make_encounter(self, level=5):
        self.encounters.add(
            Object(int(random.random() * (self.w - 500)), int(random.random() * (self.h - 100) + 50), level))

    def field_animation(self):
        key1 = True
        while key1:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: key1 = False
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_ESCAPE]:
                key1 = False
            self.clock.tick(config.gamespeed)
            self.tank.update()
            self.encounters.update()
            collided = pygame.sprite.groupcollide(self.encounters, self.tank, True, True)
            for encount in collided:
                from Battle import run_buttle
                run_buttle(encount.level)
                self.__init__()
            self.tank.draw(self.screen)
            self.encounters.draw(self.screen)
            pygame.display.flip()
