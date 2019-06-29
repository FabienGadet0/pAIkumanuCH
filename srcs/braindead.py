import random
# from grid import index_2d
from trucquibouge import get_things_around
import pandas as pd


class Brain():
    def __init__(self):
        pass

    def think(self, grid, pacu):
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
