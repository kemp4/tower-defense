import pygame

from GameCommon import GameCommon
from objects.gui.Button import Button
from objects.gui.Text import Text
from settings.Settings import MAX_LIFES, CELL_NUMBER_Y, CELL_NUMBER_X


class GuiManager:
    __gameCommon = GameCommon()

    # cash = None
    # lifes = None
    #
    # cash = None
    # lifes = None
    #
    canon = None
    is_game_over = False
    is_pause = False

    def __init__(self):
        # self.add_icon()
        # self.add_number()
        pygame.font.init()
        self.__gameCommon.font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        life = Button('heart', (10, CELL_NUMBER_Y))
        cash = Button('cash', (1, CELL_NUMBER_Y))
        life_text = Text('lifes', (11, CELL_NUMBER_Y))
        cash_text = Text('cash', (2, CELL_NUMBER_Y))
        self.canon = Button('canon', (7, CELL_NUMBER_Y))
        self.rocket_launcher = Button('rocket_launcher', (8, CELL_NUMBER_Y))
        self.slow_tower = Button('slow_tower', (9, CELL_NUMBER_Y))

        self.__gameCommon.gui_list.add([life, cash, life_text, cash_text, self.canon, self.rocket_launcher, self.slow_tower])
        # life.add(self.__gameCommon.gui_list)
        # cash.add(self.__gameCommon.gui_list)
        # life_text.add(self.__gameCommon.gui_list)
        # cash_text.add(self.__gameCommon.gui_list)

    def update(self):
        pass

    def check_click(self, mouse_position):
        if self.canon.rect.collidepoint(mouse_position):
            return 'canon'
        elif self.rocket_launcher.rect.collidepoint(mouse_position):
            return 'rocket_launcher'
        elif self.slow_tower.rect.collidepoint(mouse_position):
            return 'slow_tower'
        else:
            return ''

    def game_over(self):
        self.is_game_over = True
        game_over_text = Text('game_over', (CELL_NUMBER_X/2, CELL_NUMBER_Y/2))
        self.__gameCommon.game_variables['points_str'] = 'points:  ' + str(self.__gameCommon.game_variables['points'])  # wal
        points_text = Text('points_str', (CELL_NUMBER_X / 2, CELL_NUMBER_Y / 2 - 0.5))
        self.__gameCommon.gui_list.add(game_over_text, points_text)


