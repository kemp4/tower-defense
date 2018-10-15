import pygame
from pygame.draw import rect

from MapReader import MapReader
from objects.Enemy import Enemy
from objects.towers.Tower import Tower
from settings.Settings import WINDOW_SIZE

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tower defence")

done = False

clock = pygame.time.Clock()
tower = Tower((255,222,0), 100, 100)

towers_list = pygame.sprite.Group(tower)
# all_sprites_list = pygame.sprite.Group();

all_sprites_list = towers_list
map_elements_list = MapReader.get_map_elements()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
