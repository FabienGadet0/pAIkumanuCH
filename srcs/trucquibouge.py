import random


def get_things_around(center, grid, name=""):
    return [grid[center[1] - 1][center[0]],
            grid[center[1] + 1][center[0]], grid[center[1]][center[0] + 1], grid[center[1]][center[0] - 1]]


class Trucquibouge():
    def __init__(self, pos=[0, 0], name="truc random"):
        self.pos = pos
        self.GODHEDEAD = False  # ?
        self.name = name

    def RESTINPACURONNI(self):
        self.GODHEDEAD = True

    def COMEBACKHOLYPACU(self):
        self.GODHEDEAD = False

    def am_i_in_pacuroni(self):
        return self.GODHEDEAD

    def up(self):
        self.pos[1] -= 1

    def down(self):
        self.pos[1] += 1

    def left(self):
        self.pos[0] -= 1

    def right(self):
        self.pos[0] += 1

    def move(self, direction, thingsaround):
        dir = {'UP': self.up,
               'DOWN': self.down,
               'RIGHT': self.right,
               'LEFT': self.left}
        if (direction == 'UP' and (thingsaround[0] == 'C' or thingsaround[0] == 'V')) or \
            (direction == 'DOWN' and (thingsaround[1] == 'C' or thingsaround[1] == 'V')) or \
            (direction == 'RIGHT' and (thingsaround[2] == 'C' or thingsaround[2] == 'V')) or \
                (direction == 'LEFT' and (thingsaround[3] == 'C' or thingsaround[3] == 'V')):
            dir[direction]()
        elif (direction == 'UP' and (thingsaround[0] == 'P') or
              (direction == 'DOWN' and (thingsaround[1] == 'P')) or
              (direction == 'RIGHT' and (thingsaround[2] == 'P')) or
                (direction == 'LEFT' and (thingsaround[3] == 'P'))):
            self.RESTINPACURONNI()
            print("ITS A PACURONI {}".format(self.GODHEDEAD))
        # else:
        #     print("OH MY GOD : {}".format(self.pos))
        return self.pos

    def update(self, grid, direction="NONE"):
        return self.move(direction, get_things_around(self.pos, grid, name=self.name))

    def __str__(self):
        return "I'm {} {}, AM I DEAD : {}".format(self.name, self.pos, self.GODHEDEAD)

    def __repr__(self):
        return self.__str__()
