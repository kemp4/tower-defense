from objects.map.Grass import Grass
from objects.map.Road import Road
from objects.map.Tree import Tree


class MapElement:
    @staticmethod
    def factory(element_type, position):
        if element_type == 0:
            return Grass(position)
        if element_type == 1:
            return Road(position)
        if element_type == 2:
            return Tree(position)
        assert 0, "Bad map element type: " + element_type

    factory = staticmethod(factory)
