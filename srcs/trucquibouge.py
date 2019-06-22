import random


class Trucquibouge():
    def __init__(self, pos=[0, 0], name="truc random"):
        self.pos = pos
        self.GODHEDEAD = False  # ?
        self.name = name

    def think(self):
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def RESTINPACURONNI(self):
        self.GODHEDEAD = True

    def COMEBACKHOLYPACU(self):
        self.GODHEDEAD = False

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
        if (direction == 'UP' and not (thingsaround[0] == 'W' or thingsaround[0] == 'G')) or \
            (direction == 'DOWN' and not (thingsaround[1] == 'W' or thingsaround[1] == 'G')) or \
            (direction == 'RIGHT' and not (thingsaround[2] == 'W' or thingsaround[2] == 'G')) or \
                (direction == 'LEFT' and not (thingsaround[3] == 'W' or thingsaround[3] == 'G')):
            dir[direction]()
        else:
            print("OH MY GOD : {}".format(self.pos))
        return self.pos

    def update(self):
        print("Update {}".format(self.name))

    def __str__(self):
        return "I'm {} {}, AM I DEAD : {}".format(self.name, self.pos, self.GODHEDEAD)

    def __repr__(self):
        return self.__str__()
