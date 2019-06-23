from pacu import *
from GHOSTU.ghostu import *
from trucquibouge import GHOSTU
from GHOSTU.ZEDU import ZEDU
from GHOSTU.YGREKU import YGREKU
from GHOSTU.IXU import IXU
from GHOSTU.UUUU import UUUU

# PACU = P
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
        self.pacu = Pacu(index_2d(self.grid_, '0'))
        self.ghostu = []
        self.ghostu.append(
            UUUU(index_2d(self.grid_, GHOSTU[0]), name='UUUU', letter=GHOSTU[0]))
        self.ghostu.append(
            IXU(index_2d(self.grid_, GHOSTU[1]), name='IXU', letter=GHOSTU[1]))
        self.ghostu.append(
            YGREKU(index_2d(self.grid_, GHOSTU[2]), name='YGREKU', letter=GHOSTU[2]))
        self.ghostu.append(
            ZEDU(index_2d(self.grid_, GHOSTU[3]), name='ZEDU', letter=GHOSTU[3]))
        self.ghostu[0].is_weak = True

    def which_ghostu(self, letter):
        return self.ghostu[GHOSTU.index(letter)]

    def remove_this_trash_pacu_or_ghostu(self, letter):
        pacu_current_pos = index_2d(self.grid_, letter)
        self.grid_[pacu_current_pos[1]][pacu_current_pos[0]] = 'V'

    def update(self, direction):
        collid = self.pacu.update(self.grid_, direction=direction)
        if collid != '':
            murderer = self.which_ghostu(collid)
            if murderer.is_weak:
                murderer.die()
                print('the murderer died')
            else:
                self.pacu.die()
                print('fucking pacu ur so bad')

        self.CLEAN_THIS_TRASH_PACU()
        for g in self.ghostu:
            g.update(self.grid_)
            self.clean_ghostu(g)
        return self.pacu.is_dead

    # ? CLEAN PACU IN THE GRID
    def CLEAN_THIS_TRASH_PACU(self):
        self.remove_this_trash_pacu_or_ghostu(self.pacu.letter)
        self.grid_[self.pacu.pos[1]][self.pacu.pos[0]] = self.pacu.letter

  # ? CLEAN GHOSTU IN THE GRID
    def clean_ghostu(self, g):
        thingsaround = [self.grid_[g.pos[1] - 1][g.pos[0]],
                        self.grid_[g.pos[1] + 1][g.pos[0]], self.grid_[g.pos[1]][g.pos[0] + 1], self.grid_[g.pos[1]][g.pos[0] - 1]]
        self.remove_this_trash_pacu_or_ghostu(g.letter)
        self.grid_[g.pos[1]][g.pos[0]] = g.letter

    def __str__(self):
        return ('\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid_]))
