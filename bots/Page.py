import sys
sys.path.append("..")
import bot


class Page(bot.Bot):
    """ Class name and file name can be whatever you want, but make sure they are
    names that will be unique. Most of your code will go in the do_action() method.
    Ultimately this method will decide which action to take by setting the'action'
    variable. Feel free to add other methods and variables as long as they don't
    break the rules. """

    def __init__(self):
        """ Set some properties of your bot. """

        #######################################################################
        # Name your bot whatever you want. Your bot image should be saved as:
        # botname.png
        self.name = "Page"

        # Your reddit username
        self.creator = 'KurtJD'
        #######################################################################

        # Leave this alone
        bot.Bot.__init__(self)

    ###########################################################################
    mine_int = 30

    def do_action(self):
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

        # Write
        # a bunch
        # of code
        # here!
        if self.mine_int <= 0:
            self.action = self.ACTION_MINE
            self.mine_int = 30
        else:
            self.mine_int -= 1
            self.moveX = -1
            self.moveY = -1
            self.action = self.ACTION_MOVE
    ###########################################################################


""" Make sure to change this to your class name. This is here so that the bot
will automatically insert itself into the global bot list """
###############################################################################
Page()
###############################################################################
