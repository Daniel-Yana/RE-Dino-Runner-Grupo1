'''import random

from dino_runner.utils.constants import BIRD

from .obstacle import Obstacle
class Bird(Obstacle):
    def __init__(self, images):
        type = random.randint(0,5)
        super().__init__(images, type)
        self.rect.y = 325'''
            