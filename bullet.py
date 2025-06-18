import arena_globals
import math


class Bullet:
    """ Class detailing how a bullet operates. You should not modify this file in any way! """

    MOVE_SPEED = 7

    def __init__(self, owner_bot, startX, startY, targetX, targetY):
        self.owner_bot = owner_bot
        self.x = startX
        self.y = startY
        self.targetX = targetX
        self.targetY = targetY

        xdist = self.targetX - self.x
        ydist = self.targetY - self.y
        move_angle = math.atan2(ydist, xdist)

        self.moveX = math.cos(move_angle) * self.MOVE_SPEED
        self.moveY = math.sin(move_angle) * self.MOVE_SPEED

        arena_globals.bullets.append(self)

    def move(self):
        self.x += self.moveX
        self.y += self.moveY
