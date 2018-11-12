import pygame


class Range(pygame.sprite.Sprite):
    def __init__(self, parent_tower, *groups):
        super().__init__(*groups)
        self.position = parent_tower.position
        self.image = pygame.Surface(parent_tower.range)

