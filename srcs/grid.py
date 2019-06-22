from pacu import *
from ghostu import *

# PACU = P
# CANDYforPACU = C
# SUPER BONBON = S
# VOID = V
# WALLU = W

# GHOSTU [] :
# UUUUU = U
# IXU = X
# YGREKU = Y
# ZEDU = Z


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [x.index(v), i]


class Grid:
    def __init__(self, pathToGrid='./gridT.txt'):
        self.grid_ = []
        with open(pathToGrid) as g:
            for i in g.readlines():
                self.grid_.append(i.split())
        self.pacu = Pacu(index_2d(self.grid_, "P"))
        self.ghostu = []
        self.ghostu.append(UUUU(index_2d(self.grid_, "U")))
        self.ghostu.append(IXU(index_2d(self.grid_, "I")))
        self.ghostu.append(YGREKU(index_2d(self.grid_, "Y")))
        self.ghostu.append(ZEDU(index_2d(self.grid_, "Z")))

    def remove_this_trash_pacu_or_ghostu(self, letter):
        pacu_current_pos = index_2d(self.grid_, letter)
        self.grid_[pacu_current_pos[1]][pacu_current_pos[0]] = 'V'

    def update(self, direction):
        for g in self.ghostu:
            g.update()
        self.GETTHEFUCKOUTOFMYROOMIMPLAYING_PACU(direction)
        self.GETTHEFUCKOUTOFMYROOMIMPLAYING_GHOSTU("UP")

    # ? PACU UPDATE FUNCTION
    def GETTHEFUCKOUTOFMYROOMIMPLAYING_PACU(self, dir):
        thingsaround = [self.grid_[self.pacu.pos[1] - 1][self.pacu.pos[0]],
                        self.grid_[self.pacu.pos[1] + 1][self.pacu.pos[0]], self.grid_[self.pacu.pos[1]][self.pacu.pos[0] + 1], self.grid_[self.pacu.pos[1]][self.pacu.pos[0] - 1]]
        self.pacu.move(dir, thingsaround)
        self.ghostu[1].move(dir, thingsaround)
        self.remove_this_trash_pacu_or_ghostu('P')
        self.grid_[self.pacu.pos[1]][self.pacu.pos[0]] = 'P'

  # ? GHOSTU UPDATE FUNCTION
    def GETTHEFUCKOUTOFMYROOMIMPLAYING_GHOSTU(self, g,  dir):
        for g in self.ghostu:
            thingsaround = [self.grid_[g.pos[1] - 1][g.pos[0]],
                            self.grid_[g.pos[1] + 1][g.pos[0]], self.grid_[g.pos[1]][g.pos[0] + 1], self.grid_[g.pos[1]][g.pos[0] - 1]]
            g.move(dir, thingsaround)
            self.remove_this_trash_pacu_or_ghostu(g.name[0])
            self.grid_[g.pos[1]][g.pos[0]] = g.name[0]

    def __str__(self):
        return ('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid_]))
