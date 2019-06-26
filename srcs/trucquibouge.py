import random
import spritz

GHOSTU = '1234'


def get_things_around(center, grid, name=""):
    return [grid[center[1] - 1][center[0]],
            grid[center[1] + 1][center[0]], grid[center[1]][center[0] + 1], grid[center[1]][center[0] - 1]]


class Trucquibouge(spritz.Spritz):
    def __init__(self, pos=[0, 0], name="truc random", letter='E'):
        self.pos = pos
        self.is_dead = False  # ?
        self.name = name
        self.letter = letter
        self.direction = "RIGHT"
        super().__init__(self.pos, self.direction, "Pacu")
        # super().__init__(self.pos, self.direction, self.name)

    def die(self):
        self.is_dead = True

    def revive(self):
        self.is_dead = False

    def am_i_in_pacuroni(self):
        return self.is_dead

    def up(self):
        self.pos[1] -= 1

    def down(self):
        self.pos[1] += 1

    def left(self):
        self.pos[0] -= 1

    def right(self):
        self.pos[0] += 1

    def move(self, direction, thingsaround):
        pass

    def update(self, grid, direction="NONE"):
        return self.move(get_things_around(self.pos, grid, name=self.name), direction)

    def __str__(self):
        return "I'm {} {}, AM I DEAD : {}".format(self.name, self.pos, self.is_dead)

    def __repr__(self):
        return self.__str__()
