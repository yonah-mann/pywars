import pygame
import arena_globals


class Mine:
    """ Class detailing how a mine operates. You should not modify this file in
    any way! """

    BLAST_RADIUS = 50  # Anything caught in this radius will be damaged.
    MINE_DAMAGE = 50

    def __init__(self, owner_bot, placeX, placeY):
        self.owner_bot = owner_bot
        self.x = placeX
        self.y = placeY
        arena_globals.mines.append(self)

    def detonate(self, mine_size, bot_size):
        """ Called when a mine is stepped on. The mine explodes damaging
            everything nearby, including its owner. """

        for bot in arena_globals.bots:
            # Determine the blast boundaries
            blast_x_min = self.x - self.BLAST_RADIUS + (mine_size / 2)
            blast_x_max = self.BLAST_RADIUS
            blast_y_min = self.y - self.BLAST_RADIUS + (mine_size / 2)
            blast_y_max = self.BLAST_RADIUS
            det_rect = pygame.Rect(blast_x_min, blast_y_min,
                                   blast_x_max * 2, blast_y_max * 2)
            bot_rect = pygame.Rect(bot.x, bot.y, bot_size, bot_size)
            if det_rect.colliderect(bot_rect):
                bot.health -= self.MINE_DAMAGE
                bot.damage_taken += self.MINE_DAMAGE
                bot.last_hit_by = self.owner_bot

        arena_globals.mines.remove(self)
        # Add an explosion to the explosions list
        arena_globals.explosions.append({'x': self.x - (self.BLAST_RADIUS / 2),
                                         'y': self.y - (self.BLAST_RADIUS / 2),
                                         'count': 0})
