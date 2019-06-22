from trucquibouge import Trucquibouge, get_things_around
import random


class Ghostu(Trucquibouge):

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def think(self):
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def update(self, grid):
        self.move(self.think(), get_things_around(self.pos, grid))
