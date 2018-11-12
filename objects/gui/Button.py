import pygame

from GameCommon import GameCommon
from settings.Settings import CELL_SIZE


class Button(pygame.sprite.Sprite):
    position = (0, 0)
    color = (12, 12, 200)
    __gameCommon = GameCommon()

    def __init__(self,image_name, position):
        super().__init__()
        self.position = position
        self.image = pygame.transform.scale(self.__gameCommon.images_dict[image_name], CELL_SIZE)
        self.rect = pygame.Rect(self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0],
                                CELL_SIZE[1])

    def get_rect(self):
        return self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]

    def update(self):
        pass

    #  and event.button == LEFT_BUTTON:

    def set_highlighted(self):
        pass

    def clear_highlighted(self):
        pass
