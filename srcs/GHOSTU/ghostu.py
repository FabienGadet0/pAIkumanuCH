from trucquibouge import Trucquibouge, get_things_around
import random


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [x.index(v), i]


class Ghostu(Trucquibouge):
    def __init__(self, *args, **kwargs):
        self.is_weak = False
        self.direction = "NONE"
        return super().__init__(*args, **kwargs)

    def where_is_this_fucking_pacu(self, grid):
        return index_2d(grid, '0')

    def think(self, grid):
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def update(self, grid):
        return self.move(get_things_around(
            self.pos, grid, self.name), grid)

    # ? return cell content if collid otherwise return ''
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
            self.set_direction(direction)
        elif (direction == 'UP' and (thingsaround[0] == '0')) or(direction == 'DOWN' and (thingsaround[1] == '0')) or (direction == 'UP' and (thingsaround[2] == '0')) or (direction == 'UP' and (thingsaround[3] == '0')):
            return '0'
        return ''
