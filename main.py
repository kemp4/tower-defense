import os

import pygame
from pygame.sprite import Sprite

from MapReader import MapReader
from settings.Settings import WINDOW_SIZE

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.SRCALPHA)
pygame.display.set_caption("Tower defence")

done = False

clock = pygame.time.Clock()
# tower = Tower((255, 222, 0), 100, 100)

# towers_list = pygame.sprite.Group(tower)

# t = Tower(color=(122, 23, 231), width=100, height=100)
# t.rect = (100, 100, 100, 100)
# towers_list.add(t)

# all_sprites_list = pygame.sprite.Group();

# all_sprites_list = towers_list

map_elements_list = MapReader().get_map_elements()

all_sprites_list = map_elements_list
print(map_elements_list)
pygame.mouse.set_visible(False)
# print(os.path.join('data', 'bla.png'))
mouse = pygame.image.load(os.path.join('assets', 'gui', 'mouse.png')).convert_alpha()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEMOTION:
            print('mouse at (%d, %d)' % event.pos)

#     if box.rect.collidepoint(x,y): print 'yay!'
    for sprite in all_sprites_list:
        if sprite.rect.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            print(sprite)

    all_sprites_list.draw(screen)
    screen.blit(mouse, pygame.mouse.get_pos())
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
