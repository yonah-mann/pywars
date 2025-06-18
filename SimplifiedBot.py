import arena_globals
from bot import Bot


class SimplifiedBot(Bot):
    def move_right(self):
        self.moveX = 1
        self.moveY = 0
        self.action = self.ACTION_MOVE

    def move_left(self):
        self.moveX = -1
        self.moveY = 0
        self.action = self.ACTION_MOVE

    def move_up(self):
        self.moveX = 0
        self.moveY = -1
        self.action = self.ACTION_MOVE

    def move_down(self):
        self.moveX = 0
        self.moveY = 1
        self.action = self.ACTION_MOVE
