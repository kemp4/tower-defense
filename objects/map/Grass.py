import pygame

from settings.Settings import CELL_SIZE


class Grass(pygame.sprite.Sprite):
    COLOR = (155, 244, 66)

    def __init__(self, position):
        super().__init__()
        self.image = pygame.Surface([CELL_SIZE])
        self.image.fill(self.COLOR)
        pygame.draw.ellipse(self.image, self.COLOR, [position, CELL_SIZE])
        self.rect = self.image.get_rect()
