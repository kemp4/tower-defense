from pygame.sprite import Group

from settings.Settings import MAX_LIFES, START_CASH


class GameCommon(object):
    class __GameCommon:
        def __init__(self):
            self.route = None
            # self.lifes = MAX_LIFES
            # self.cash = START_CASH
            self.enemies_list = Group()
            self.towers_list = Group()
            self.bullets_list = Group()
            self.gui_list = Group()
            self.temp_group = Group()
            self.images_dict = {}
            self.font = None
            self.game_variables = {'lifes': MAX_LIFES, 'cash': START_CASH, 'points': 0, 'game_over': 'Game Over'
                                   }
            self.highlightable = Group()
            self.highlighted = Group()
            self.ranges = Group()

            # self.cash_surface = None
            # self.lifes_surface = None

    instance = None

    def __new__(cls):
        if not GameCommon.instance:
            GameCommon.instance = GameCommon.__GameCommon()
        return GameCommon.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, **kwargs):
        return setattr(self.instance, name)

