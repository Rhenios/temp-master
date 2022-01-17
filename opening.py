import pygame

import config
from box.object.button import Button
from config import width, height


def opening_animation():

    screen = pygame.display.set_mode((width, height))
    key2 = True
    buttons = pygame.sprite.Group()
    buttons.add(
        Button((width / 2 - 100, height / 2 - 200), 50, 10, (255, 255, 255), (0, 0, 0), "welcome to my game world",screen))
    buttons.add(Button((width / 2, height / 2), 30, 10, (255, 255, 255), (0, 0, 0), "new game", screen, "field"))
    buttons.add(Button((width / 2, height / 2 + 200), 30, 10, (255, 255, 255), (0, 0, 0), "exit", screen, "exit"))
    while key2:
        screen.fill((0, 0, 0))
        pygame.time.Clock().tick(config.gamespeed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: key2 = False
        for i,a in enumerate(buttons):
            if a.update() and a.object == "field": return "field"
            if a.update() and a.object == "exit": return "exit"
        buttons.update()
        pygame.display.flip()
    pygame.quit()
    return False
