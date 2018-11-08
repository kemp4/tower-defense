import pygame

from objects.map.MapElement import MapElement
from settings.Settings import CELL_SIZE


class Grass(MapElement):
    COLOR = (155, 244, 66)
    HIGHLIGHTED_COLOR = (188, 255, 99)

    def __init__(self, position):
        super(Grass, self).__init__(position, self.COLOR)

    def set_highlighted(self):
        self.image.fill(self.HIGHLIGHTED_COLOR)

    def clear_highlighted(self):
        self.image.fill(self.COLOR)

