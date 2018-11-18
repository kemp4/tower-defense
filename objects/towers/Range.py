import pygame

from GameCommon import GameCommon
from settings.Settings import CELL_SIZE

RANGE_SURF = pygame.Surface((CELL_SIZE[0] * 2, CELL_SIZE[1] * 2))
RANGE_SURF.set_colorkey((0, 0, 0))
RANGE_SURF.set_alpha(56)
pygame.draw.circle(RANGE_SURF, (0, 255, 0), CELL_SIZE, 50)


class Range:
    gameCommon = GameCommon()
    # COLOR = pygame.Color(111, 2, 133, 0.2)
    parent_tower = None

    class __Range(pygame.sprite.Sprite):
        position = pygame.Vector2()
        image = None
        rect = None

        def __init__(self, *groups):
            super().__init__(*groups)
            self.update()
            Range.gameCommon.ranges.add_internal(self)
            self.add(Range.gameCommon.ranges)

        def get_rect(self):
            return (self.position[0] - Range.parent_tower.range + 0.5) * CELL_SIZE[0], \
                   (self.position[1] - Range.parent_tower.range + 0.5) * CELL_SIZE[1], \
                   CELL_SIZE[0] * Range.parent_tower.range, \
                   CELL_SIZE[1] * Range.parent_tower.range

        def __update(self):
            self.position = Range.parent_tower.position
            self.image = RANGE_SURF
            # self.image = pygame.transform.scale(self.image, pygame.Vector2(CELL_SIZE * parent_tower.range))  #refactor
            self.image = pygame.transform.scale(self.image,
                                                (Range.parent_tower.range * CELL_SIZE[0]*2,
                                                 Range.parent_tower.range * CELL_SIZE[1]*2))
            self.rect = self.get_rect()

        def __disable(self):
            self.rect = (-1000, -1000, 0, 0)

    instance = None

    def __new__(cls, parent_tower):
        Range.parent_tower = parent_tower
        if not Range.instance:
            Range.instance = Range.__Range()
        Range.instance.__update()
        return Range.instance

    @staticmethod
    def disable():
        if Range.instance:
            Range.instance.__disable()
