import random


class Brain():
    def __init__(self):
        pass

    def think(self, grid):
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
