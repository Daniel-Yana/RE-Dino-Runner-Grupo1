import random
from .obstacle import Obstacle
class Cactus(Obstacle):
    def __init__(self, images):
        type = random.randint(0,5)
        super().__init__(images, type)
        self.rect.y = 325
