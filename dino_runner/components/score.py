import pygame

from dino_runner.utils.constants import FONT_STYLE


class Score():
    def __init__(self):
        self.score = 0

    def update(self, game):
        self.score +=1
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        scores = font.render(f"Points: {self.score}", True, (0,0,0) )
        text_rect = scores.get_rect()
        text_rect.center = (1000 ,50)
        screen.blit(scores, text_rect)

    def reset_score(self, game):
        self.score = 0
        game.game_speed = 20