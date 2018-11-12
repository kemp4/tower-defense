import pygame

from GameCommon import GameCommon
from settings.Settings import CELL_SIZE


class Text(pygame.sprite.Sprite):
    position = (0, 0)
    color = (12, 12, 200)
    __gameCommon = GameCommon()
    variable_name = ''
    image = None  # = __gameCommon.font.render('0'), False, (0, 0, 0))

    def __init__(self, variable_name, position):
        super().__init__()
        self.variable_name = variable_name
        self.position = position
        self.rect = pygame.Rect(self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0],
                                CELL_SIZE[1])

    def get_rect(self):
        return self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]

    def update(self):
        self.image = self.__gameCommon.font.render(str(self.__gameCommon.game_variables[self.variable_name]), False, (0, 0, 0))

    #  and event.button == LEFT_BUTTON:

    def set_highlighted(self):
        pass

    def clear_highlighted(self):
        pass
