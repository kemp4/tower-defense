import pygame

from settings.Settings import CELL_SIZE


class MapElement(pygame.sprite.Sprite):
    position = (0, 0)

    def __init__(self, position, color):
        super().__init__()
        self.position = position
        self.image = pygame.Surface(CELL_SIZE)
        self.image.fill(color)
        self.rect = pygame.Rect(self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0],
                                CELL_SIZE[1])
        # print("pos_X " + str(position[0]) + " pos_Y " + str(position[1]) + "TYPE = " + str(color))
        # pygame.draw.rect(self.image, color, [300, 300, 50, 50])
        # pygame.draw.ellipse(self.image, self.COLOR, position, 1)
        # self.rect = self.get_position()

    def get_rect(self):
        return self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]

    def set_highlighted(self):
        pass

    def clear_highlighted(self):
        pass
