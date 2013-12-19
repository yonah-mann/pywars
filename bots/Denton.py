import sys
sys.path.append("..")
import bot
import arena_globals
import math

""" Class name and file name can be whatever you want, but make sure they are
names that will be unique. Most of your code will go in the do_action() method.
Ultimately this method will decide which action to take by setting the'action'
variable. Feel free to add other methods and variables as long as they don't
break the rules. """
class Denton(bot.Bot):
    def __init__(self):

        """ Set some properties of your bot. """
        #######################################################################
        # Name your bot whatever you want. Your bot image should be saved as:
        # botname.png
        self.name = "Denton"

        # Your reddit username
        self.creator = 'KurtJD'
        #######################################################################

        # Leave this alone
        bot.Bot.__init__(self)


    """
    All thinking goes here. This will be the bulk of your code.
        Actions can be set to:

            ACTION_MOVE -   Move at a rate of MOVE_SPEED in the directions
                            specified in self.moveX and self.moveY

            ACTION_SHOOT -  Shoot a bullet at the coordinates specified in
                            self.shootAtX and self.shootAtY

            ACTION_HEAL -   Heals one point of health up to MAX_HEALTH
            ACTION_RELOAD - Reloads one bullet up to MAX_AMMO
            ACTION_MINE -   Places a mine on bot's x and y coordinates
            ACTION_WALL -   Places a wall on bot's x and y coordinates
    """
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
        # Write
        # a bunch
        # of code
        # here!
        self.say('Take your best shot.')
        if self.health < 30:
            self.action = self.ACTION_HEAL
        elif self.action != self.ACTION_SHOOT and self.action != self.ACTION_RELOAD:
            if not self.close_bot():
                self.moveX = 1
                self.moveY = -1
                self.action = self.ACTION_MOVE
        elif self.action == self.ACTION_SHOOT:
            if self.ammo == 0:
                self.action = self.ACTION_RELOAD
        elif self.action == self.ACTION_RELOAD:
            if self.ammo == self.MAX_AMMO:
                self.action = self.ACTION_MOVE
    ###########################################################################


    """ The victory_dance() method is called if your bot wins a match. Since it
    is only called at the end, do whatever you want in here. Go crazy! """
    ###########################################################################
    def victory_dance(self):
        pass
    ###########################################################################

""" Make sure to change this to your class name. This is here so that the bot
will automatically insert itself into the global bot list """
###############################################################################
Denton()
###############################################################################