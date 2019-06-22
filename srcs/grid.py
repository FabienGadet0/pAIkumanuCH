P = 1  # PACU
G = 2  # GHOSTU
C = 3  # CANDYforPACU
W = 4  # WALLU


class Grid:

    def __init__(self):
        self.grid_ = []
        with open('./gridT.txt') as g:
            for i in g.readlines():
                self.grid_.append(i)

    def __str__(self):
        return ('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid_]))


# Exemple, print la grille
if __name__ == "__main__":
    a = Grid()
    print(a)
