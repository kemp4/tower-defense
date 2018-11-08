import os

import pygame

from MapReader import MapReader
from objects.Enemy import Enemy
from objects.gui.Gui import Gui
from settings.Settings import WINDOW_SIZE

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.SRCALPHA)
pygame.display.set_caption("Tower defence")

done = False

clock = pygame.time.Clock()

gui = Gui()
gui_elements_list = gui.get_gui_elements()
enemy = Enemy((4, 1))

map_elements_list = MapReader().get_map_elements()

all_sprites_list = map_elements_list
all_sprites_list.add_internal(enemy)
# print(map_elements_list)
pygame.mouse.set_visible(False)
mouse = pygame.image.load(os.path.join('assets', 'gui', 'mouse.png')).convert_alpha()

while not done:
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            pass
            # if event.type == pygame.MOUSEMOTION:
            # print('mouse at (%d, %d)' % event.pos)

    for sprite in all_sprites_list:
        if sprite.rect.collidepoint(mouse_position):
            sprite.set_highlighted()
        else:
            sprite.clear_highlighted()

    all_sprites_list.draw(screen)
    screen.blit(mouse, mouse_position)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
