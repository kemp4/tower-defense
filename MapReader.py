import pygame

from objects.map.map_elements_factory_method import map_element_factory


class MapReader:
    MAP = [
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def get_map_elements(self):

        map_elements_list = pygame.sprite.Group()
        for i in range(len(self.MAP)):
            for j in range(len(self.MAP[i])):
                # map_elements_list.add(map_element_factory(self.MAP[i][j], (i, j)))
                map_elements_list.add(map_element_factory(self.MAP[i][j], (i, j)))
                # get_map_elements = staticmethod(get_map_elements)

        return map_elements_list
