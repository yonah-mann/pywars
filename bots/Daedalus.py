import sys
sys.path.append("..")
import bot
import arena_globals
# You may import built-in modules. No external modules though!
import math


class Daedalus(bot.Bot):
    """
    Class name and file name can be whatever you want, but make sure they are names
    that will be unique.

    Most of your code will go in the do_action() method. Ultimately this method
    will decide which action to take by setting the 'self.action' variable.

    Feel free to add other classes, methods, and variables as long as they don't
    break the rules.

    However, all code must be contained within this file. The only other file you
    should create is the image file for your bot.
    """

    def __init__(self):
        """ Set some properties of your bot. """

        #######################################################################
        # Name your bot. Max 10 characters.
        # Your bot image should be saved as: botname.jpg
        self.set_name('Daedalus')

        # Your reddit username. Max 15 characters.
        self.set_creator('The_Chosen_One')
        #######################################################################
        bot.Bot.__init__(self)

    ###########################################################################
    def close_bot(self):
        for bot in arena_globals.bots:
            if bot is not self:
                if abs(bot.x - self.x) < 300 and abs(bot.y - self.y) < 300:
                    self.shootAtX = bot.x
                    self.shootAtY = bot.y
                    self.action = self.ACTION_SHOOT
                    return True
        return False

    def do_action(self):
        """
            All thinking goes here. This will be the bulk of your code.
                self.action can be set to:

                    self.ACTION_MOVE -   Move at a rate of MOVE_SPEED in the directions
                                         specified in self.moveX and self.moveY

                    self.ACTION_SHOOT -  Shoot a bullet at the coordinates specified in
                                         self.shootAtX and self.shootAtY

                    self.ACTION_HEAL -   Heals one point of health up to MAX_HEALTH

                    self.ACTION_RELOAD - Reloads one bullet up to MAX_AMMO

                    self.ACTION_MINE -   Places a mine on bot's x and y coordinates

            Remember:
                -A list of bots can be accessed by arena_globals.bots
                -A list of bullets can be accessed by arena_globals.bullets
                -A list of mines can be accessed by arena_globals.mines
            """

        # Write
        # a bunch
        # of code
        # here!
        if self.health < 30 and self.action != self.ACTION_HEAL:
            self.action = self.ACTION_HEAL
        elif self.action == self.ACTION_HEAL:
            if self.health == self.MAX_HEALTH:
                self.action = self.ACTION_MOVE
        elif self.action != self.ACTION_SHOOT and self.action != self.ACTION_RELOAD:
            if not self.close_bot():
                xdist = arena_globals.bots[1].x - self.x
                ydist = arena_globals.bots[1].y - self.y
                move_angle = math.atan2(ydist, xdist)

                self.moveX = math.cos(move_angle)
                self.moveY = math.sin(move_angle)

                self.action = self.ACTION_MOVE
        elif self.action == self.ACTION_SHOOT:
            if self.ammo == 0:
                self.action = self.ACTION_RELOAD
        elif self.action == self.ACTION_RELOAD:
            if self.ammo == self.MAX_AMMO:
                self.action = self.ACTION_MOVE
    ###########################################################################


"""
Make sure to change this to your class name. This is here so that the bot
will automatically insert itself into the global bot list.
"""
###############################################################################
Daedalus()
###############################################################################
