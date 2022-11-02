import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactusl import CactusL
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager:
    def __init__ (self):
        self.obstacles = []
        self.cactuss = SMALL_CACTUS + LARGE_CACTUS
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(self.cactuss))
            #self.obstacles.append(CactusL(LARGE_CACTUS))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, game):
        for obstacle in self.obstacles:
            obstacle.draw(game.screen)