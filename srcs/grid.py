from pacu import *
from GHOSTU.ghostu import *
from GHOSTU.ZEDU import ZEDU
from GHOSTU.YGREKU import YGREKU
from GHOSTU.IXU import IXU
from GHOSTU.UUUU import UUUU

# PACU = P
# CANDYforPACU = C
# SUPER BONBON = S
# VOID = V
# WALLU = W

# GHOSTU [] :
# UUUUU = U
# IXU = I
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
        self.pacu.update(self.grid_, direction=direction)
        self.clean_pacu()
        for g in self.ghostu:
            g.update(self.grid_)
            self.clean_ghostu(g)
        return any(x.GODHEDEAD for x in self.ghostu)

    # ? CLEAN PACU IN THE GRID
    def clean_pacu(self):
        self.remove_this_trash_pacu_or_ghostu('P')
        self.grid_[self.pacu.pos[1]][self.pacu.pos[0]] = 'P'

  # ? CLEAN GHOSTU IN THE GRID
    def clean_ghostu(self, g):
        thingsaround = [self.grid_[g.pos[1] - 1][g.pos[0]],
                        self.grid_[g.pos[1] + 1][g.pos[0]], self.grid_[g.pos[1]][g.pos[0] + 1], self.grid_[g.pos[1]][g.pos[0] - 1]]
        g.move(g.think(), thingsaround)
        self.remove_this_trash_pacu_or_ghostu(g.name[0])
        self.grid_[g.pos[1]][g.pos[0]] = g.name[0]

    def __str__(self):
        return ('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid_]))
