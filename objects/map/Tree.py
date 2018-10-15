import pygame

from objects.map.MapElement import MapElement


class Tree(MapElement):
    COLOR = (102, 51, 0)

    def __init__(self, position):
        super(Tree, self).__init__(position, self.COLOR)
