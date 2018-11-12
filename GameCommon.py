from pygame.sprite import Group


class GameCommon(object):
    class __GameCommon:
        def __init__(self):
            self.route = None
            self.lifes = 20
            self.enemies_list = Group()
            self.towers_list = Group()
            self.bullets_list = Group()
            self.images_dict = {}
            self.temp_group = Group()

    instance = None

    def __new__(cls):
        if not GameCommon.instance:
            GameCommon.instance = GameCommon.__GameCommon()
        return GameCommon.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, **kwargs):
        return setattr(self.instance, name)

