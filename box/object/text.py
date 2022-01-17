import sys

import pygame
from pygame.rect import Rect


class Text(pygame.sprite.Sprite):
    def __init__(self, pos, size, pad, color, txtcolor, text="Button",screen = pygame.display.set_mode((1,1)),object=None):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.screen = screen
        self.pad = pad
        self.color = color
        self.font = pygame.font.SysFont("/box/font/HGRGE.TTC", size)
        self.text = self.font.render(text, True, txtcolor)
        self.button = Rect(pos, (self.text.get_width() + pad, self.text.get_height() + pad))
        self.button_bottom = Rect(pos, (self.button.width, self.button.height + 5))
        self.object = object

    def update(self):
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.button)
        self.screen.blit(self.text, (self.x + self.pad / 2, self.y + self.pad / 2))