from GameCommon import GameCommon
from objects.map.MapElement import MapElement


class Grass(MapElement):
    COLOR = (155, 244, 66)
    HIGHLIGHTED_COLOR = (188, 255, 99)
    __gameCommon = GameCommon()
    tower = None

    def __init__(self, position):
        super(Grass, self).__init__(position, self.COLOR)
        self.__gameCommon.highlightable.add_internal(self)
        self.add(self.__gameCommon.highlightable)

    def set_highlighted(self):
        self.image.fill(self.HIGHLIGHTED_COLOR)
        if self.tower is not None:
            self.tower.set_highlighted()

    def clear_highlighted(self):
        self.image.fill(self.COLOR)
        if self.tower is not None:
            self.tower.clear_highlighted()

    def set_tower(self, tower):
        self.tower = tower

    def is_free(self):
        return self.tower is None
