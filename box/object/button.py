import sys

import pygame
from pygame.rect import Rect


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, pad, color, txtcolor, text="Button",screen = pygame.display.set_mode((1,1)),object=None):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.key = False
        self.screen = screen
        self.pad = pad
        self.color = color
        try:
            self.font = pygame.font.SysFont("/box/font/HGRGE.TTC", size)
            self.text = self.font.render(text, True, txtcolor)
        except Exception as e:
            print(e)
        self.button = Rect(pos, (self.text.get_width() + pad, self.text.get_height() + pad))
        self.button_bottom = Rect(pos, (self.button.width, self.button.height + 5))
        self.object = object

    def update(self):
        self.button.top = self.y

        if pygame.mouse.get_pressed()[0]:
            if self.button.collidepoint(pygame.mouse.get_pos()):
                self.button.top += 2
                self.key = True
                try:
                    self.object()
                except:
                    pass
        else:
            self.key = False
        self.draw()
        return self.key

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.button)
        self.screen.blit(self.text, (self.x + self.pad / 2, self.y + self.pad / 2))

    def check(self):
        return self.key