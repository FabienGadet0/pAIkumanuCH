import numpy as np


class Grid:

    def __init__(self):
        P = 1  # PACU
        G = 2  # GHOSTU
        C = 3  # CANDYforPACU
        W = 4  # WALLU
        self.grid_ = [[W, W, W, W, W, W, W, W],
                      [C, C, C, C, C, W, W, W],
                      [C, C, C, W, W, W, C, C],
                      [C, C, C, P, C, G, G, G]]

    def __str__(self):
        return ('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid_]))


# Example , print la grille
if __name__ == "__main__":
    a = Grid()
    print(a)
