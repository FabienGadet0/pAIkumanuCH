from grid import *
import os
import graphics as g

if __name__ == "__main__":
    gridu = Grid()
    graphics = g.Graphics()
    print("Hi i'm pAIkumanuCH, here is the team : ")

    print(gridu.pacu)
    print(gridu.ghostu)
    print()
    print("And the grid :")
    print(gridu)
    while 1:
        graphics.draw_this_shit(gridu.grid_)
        gridu.update()
