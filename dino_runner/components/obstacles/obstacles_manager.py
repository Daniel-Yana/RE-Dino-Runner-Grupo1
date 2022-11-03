import random
import pygame
#from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD


class ObstacleManager:
    def __init__ (self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            option = random.randint(0,2)
            if (option == 0):
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif (option == 1):
                self.obstacles.append(Cactus(LARGE_CACTUS))

                
        

        

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, game):
        for obstacle in self.obstacles:
            obstacle.draw(game.screen)

    def reset_obstacles(self):
        self.obstacles = []