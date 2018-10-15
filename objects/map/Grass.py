import pygame

from objects.map.MapElement import MapElement
from settings.Settings import CELL_SIZE


class Grass(MapElement):
    COLOR = (155, 244, 66)

    def __init__(self, position):
        super(Grass, self).__init__(position, self.COLOR)
