from pacu import *

# PACU = P
# GHOSTU = G
# CANDYforPACU = C
# SUPER BONBON = S
# VOID = V
# WALLU = W


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

    def remove_this_trash_pacu(self):
        pacu_current_pos = index_2d(self.grid_, "P")
        self.grid_[pacu_current_pos[1]][pacu_current_pos[0]] = 'V'

    def GETTHEFUCKOUTOFMYROOMIMPLAYING_PACU(self, dir):
        thingsaround = [self.grid_[self.pacu.pos[1] - 1][self.pacu.pos[0]],
                        self.grid_[self.pacu.pos[1] + 1][self.pacu.pos[0]], self.grid_[self.pacu.pos[1]][self.pacu.pos[0] + 1], self.grid_[self.pacu.pos[1]][self.pacu.pos[0] - 1]]
        self.pacu.move(dir, thingsaround)
        self.remove_this_trash_pacu()
        self.grid_[self.pacu.pos[1]][self.pacu.pos[0]] = 'P'

    def __str__(self):
        return ('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid_]))
