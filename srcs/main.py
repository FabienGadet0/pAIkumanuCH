from grid import *
import os
import graphics as g
import pygame

if __name__ == "__main__":
    gridu = Grid()
    graphics = g.Graphics()
    print("Hi i'm pAIkumanuCH, here is the team : ")

    ending = False
    clock = pygame.time.Clock()
    while not ending:
        clock.tick(5)
        key = graphics.get_last_key()
        ending = gridu.update(key)
        graphics.draw_this_shit(gridu.grid_)
