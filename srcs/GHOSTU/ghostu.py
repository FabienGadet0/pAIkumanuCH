from trucquibouge import Trucquibouge, get_things_around
import random


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [x.index(v), i]


class Ghostu(Trucquibouge):

    def __init__(self, *args, **kwargs):
        self.is_weak = False
        return super().__init__(*args, **kwargs)

    def where_is_this_fucking_pacu(self, grid):
        return index_2d(grid, '0')

    def think(self, grid):
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def update(self, grid):
        self.move(get_things_around(
            self.pos, grid, self.name), grid)

    def move(self, thingsaround, grid):
        direction = self.think(grid)
        dir = {'UP': self.up,
               'DOWN': self.down,
               'RIGHT': self.right,
               'LEFT': self.left}
        if (direction == 'UP' and (thingsaround[0] in 'CV') or
            (direction == 'DOWN' and (thingsaround[1] in 'CV')) or
            (direction == 'RIGHT' and (thingsaround[2] in 'CV')) or
                (direction == 'LEFT' and (thingsaround[3] in 'CV'))):
            dir[direction]()
        elif ((direction == 'UP' and (thingsaround[0] == '0') or
               (direction == 'DOWN' and (thingsaround[1] == '0')) or
               (direction == 'RIGHT' and (thingsaround[2] == '0')) or
                (direction == 'LEFT' and (thingsaround[3] == '0'))) and self.is_weak):
            self.die()
            print("{} has been killed by Pacu".format(self.name))
        return self.pos