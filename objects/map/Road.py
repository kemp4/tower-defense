import pygame

from objects.map.MapElement import MapElement


class Road(MapElement):
    COLOR = (122, 122, 122)

    def __init__(self, position):
        super(Road, self).__init__(position, self.COLOR)
