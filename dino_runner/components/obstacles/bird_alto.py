'''import random

from dino_runner.utils.constants import BIRD

from .obstacle import Obstacle
class Bird(Obstacle):
    def __init__(self, images):
        type = random.randint(0,5)
        super().__init__(images, type)
        self.rect.y = random.randint(325, 200)'''


import random

from dino_runner.utils.constants import BIRD
from .obstacle import Obstacle
class Bird(Obstacle):
    POST = 240
    def __init__(self, images):
        type = 0
        super().__init__(images, type)
        self.rect.y = self.POST
        
