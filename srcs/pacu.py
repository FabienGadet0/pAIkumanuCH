from trucquibouge import Trucquibouge, GHOSTU, get_things_around
from braindead import Brain


class Pacu(Trucquibouge):
    def __init__(self, pos=[0, 0], letter='0'):
        super().__init__(pos, 'Pacu', letter=letter)
        self.brain = Brain()

    def update(self, grid, direction="NONE", AI=False):
        if AI:
            direction = self.brain.think(grid)
        return self.move(get_things_around(self.pos, grid, name=self.name), direction)

# ? return cell content if collid otherwise return ''
    def move(self, thingsaround, direction):
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
            self.set_sprite_pos(self.pos)
        elif (direction == 'UP' and (thingsaround[0] in GHOSTU)):
            return thingsaround[0]
        elif (direction == 'DOWN' and (thingsaround[1] in GHOSTU)):
            return thingsaround[1]
        elif (direction == 'UP' and (thingsaround[2] in GHOSTU)):
            return thingsaround[2]
        elif (direction == 'UP' and (thingsaround[3] in GHOSTU)):
            return thingsaround[3]
        return ''
