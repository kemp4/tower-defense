import pygame

from GameCommon import GameCommon
from objects.gui.Button import Button
from objects.gui.Text import Text
from settings.Settings import MAX_LIFES, CELL_NUMBER_Y


class GuiManager:
    __gameCommon = GameCommon()

    # cash = None
    # lifes = None
    #
    # cash = None
    # lifes = None
    #
    canon = None

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
        self.__gameCommon.gui_list.add([life, cash, life_text, cash_text, self.canon])
        # life.add(self.__gameCommon.gui_list)
        # cash.add(self.__gameCommon.gui_list)
        # life_text.add(self.__gameCommon.gui_list)
        # cash_text.add(self.__gameCommon.gui_list)

    def update(self):
        pass

    def check_click(self, mouse_position):
        if self.canon.rect.collidepoint(mouse_position):
            print('canon choosed')
            return 'canon'
        else:
            return ''
