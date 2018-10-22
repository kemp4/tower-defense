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

    START_POINT = (4, 0)
    END_POINT = (4, 12)

    NEIGHBORS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def get_map_elements(self):
        map_elements_list = pygame.sprite.Group()
        for i in range(len(self.MAP[0])):
            for j in range(len(self.MAP)):
                # map_elements_list.add(map_element_factory(self.MAP[i][j], (i, j)))
                map_elements_list.add(map_element_factory(self.MAP[j][i], (i, j)))
                # get_map_elements = staticmethod(get_map_elements)
        self.get_route()
        return map_elements_list

    def get_route(self):
        route = []
        actual_point = self.START_POINT
        old_actual_point = actual_point
        while actual_point != self.END_POINT:
            road_neighbors = self.get_road_neighbors(actual_point)
            # new_actual_point = None
            if len(road_neighbors) > 2:
                raise ValueError('MAP file is not proper (MAP nr: 0)')
            if len(road_neighbors) == 1:
                new_actual_point = road_neighbors[0]
            if len(road_neighbors) > 1:
                new_actual_point = (road_neighbors[0] if old_actual_point != road_neighbors[0] else road_neighbors[1])
            route.append(new_actual_point)
            old_actual_point = actual_point
            actual_point = new_actual_point

        print(route)

    def get_road_neighbors(self, point):
        neighbors = []
        for neighbor_offset in self.NEIGHBORS:
            neighbors.extend(
                self.get_road_element_as_list((point[0] + neighbor_offset[0], point[1] + neighbor_offset[1])))
        return neighbors

    def get_road_element_as_list(self, point):
        if (point[0] >= 0) and (point[0] < len(self.MAP)) and (point[1] >= 0) and (point[1] < len(self.MAP[0])):
            if self.MAP[point[0]][point[1]] == 1:
                return [point]
        return []
