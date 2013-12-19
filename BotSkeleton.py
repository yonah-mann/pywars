import sys
sys.path.append('..')
import bot
import arena_globals
# You may import built-in modules. No external modules though!


"""
This is the skeleton class for your bot. Modify it to suit your needs keeping
in mind the following:

Class name and file name can be whatever you want, but make sure they are names
that will be unique.

Most of your code will go in the do_action() method. Ultimately this method
will decide which action to take by setting the 'self.action' variable.

Feel free to add other classes, methods, and variables as long as they don't
break the rules.

However, all code must be contained within this file. The only other file you
should create is the image file for your bot. Remember to save this file in the
'bots' subfolder.
"""
class CHANGE_ME(bot.Bot):
    def __init__(self):
        """ Set some properties of your bot. """
        #######################################################################
        # Name your bot. Max 10 characters.
        # Your bot image should be saved as: BotName.jpg in the 'images' folder
        self.set_name('CHANGE_ME')

        # Your username. Max 15 characters.
        self.set_creator('CHANGE_ME')
        #######################################################################
        bot.Bot.__init__(self)

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

    Besides ones you created yourself, you may only modify these variables:
        self.action
        self.moveX
        self.moveY
        self.shootAtX
        self.shootAtY
    Consult bot.py or the README if you are confused as to what these do.

    Remember:
        -A list of bots can be accessed by arena_globals.bots
        -A list of bullets can be accessed by arena_globals.bullets
        -A list of mines can be accessed by arena_globals.mines
        -Consult the README for more information
    """
    ###########################################################################
    def do_action(self):
        # Write
        # a bunch
        # of code
        # here!
        pass
    ###########################################################################

    """
    The victory_dance() method is called if your bot wins a match. Since it
    is only called at the end, do whatever you want in here. Go crazy!
    """
    ###########################################################################
    def victory_dance(self):
        # Write
        # a bunch
        # of code
        # here!
        pass
    ###########################################################################

"""
Make sure to change this to your class name. This is here so that the bot
will automatically insert itself into the global bot list.
"""
###############################################################################
CHANGE_ME()
###############################################################################