import inspect


class BasePlayer:
    def __init__(self):
        self.field_type = None

    def choose_field(self, grid):
        raise NotImplementedError(str(inspect.stack()[1][3]))

    def after_decision(self, grid, game_state):
        pass

    def __str__(self):
        return '<Player:{}>'.format(self.field_type.name)
