import sys
import pygame
from Battle import run_buttle
from field import run_field
from opening import opening_animation


def exit():
    pygame.quit()
    sys.exit()

def run():
    pygame.init()
    key = True
    state = "opening"
    while key:
        match state:
            case "opening":
                state = opening_animation()
            case "field":
                state = run_field()
            case _:
                key = False


