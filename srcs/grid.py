# PACU = P
# GHOSTU = G
# CANDYforPACU = C
# WALLU = W


class Grid:
    def __init__(self, pathToGrid='./gridT.txt'):
        self.grid_ = []
        with open(pathToGrid) as g:
            for i in g.readlines():
                self.grid_.append(i)

    def __str__(self):
        return ('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid_]))


# Exemple, print la grille
if __name__ == "__main__":
    a = Grid()
    print(a)
