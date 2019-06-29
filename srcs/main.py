import grid
import os
import graphics
import pygame

FRAME_RATE = 200
if __name__ == "__main__":
    graphics = graphics.Graphics()
    gridu = grid.Grid()
    print("Hi i'm pAIkumanuCH, here is the team : ")

    ending = False
    clock = pygame.time.Clock()
    milliseconds = clock.tick(FRAME_RATE)
    while not ending:
        key = graphics.get_last_key()
        if milliseconds > 150:
            ending = gridu.update(key)
            milliseconds = clock.tick(FRAME_RATE)
        milliseconds += clock.tick(FRAME_RATE)
        graphics.draw_this_shit(gridu)
