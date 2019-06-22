from grid import *
import os
import graphics as g
import pygame

if __name__ == "__main__":
    gridu = Grid()
    graphics = g.Graphics()
    print("Hi i'm pAIkumanuCH, here is the team : ")

    print(gridu.pacu)
    print(gridu.ghostu)
    print()
    print("And the grid :")
    print(gridu)
    clock = pygame.time.Clock()
    while 1:
        clock.tick(5)
        key = graphics.get_last_key()
        gridu.update(key)
        graphics.draw_this_shit(gridu.grid_)
