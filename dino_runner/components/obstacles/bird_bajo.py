import random

from dino_runner.utils.constants import BIRD
from .obstacle import Obstacle
class Birds(Obstacle):
    POST = 100
    def __init__(self, images):
        type = 1
        super().__init__(images, type)
        self.rect.y = self.POST
        