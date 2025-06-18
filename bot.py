import arena_globals


class Bot:
    """ The base class from which all bots inherit. No code should be written in
    here, nor should any code be modified in here. """

    # Bot constants. DO NOT MODIFY!
    MAX_HEALTH = 100
    MAX_AMMO = 20
    MOVE_SPEED = arena_globals.GRID_SIZE
    MAX_MINES = 5

    # List of possible actions. DO NOT MODIFY!
    ACTION_MOVE = 1
    ACTION_SHOOT = 2
    ACTION_HEAL = 3
    ACTION_RELOAD = 4
    ACTION_MINE = 5

    def __init__(self):
        """ These are the only variables you can manipulate. """
        #######################################################################
        # The action your bot will take for the current frame
        self.action = self.ACTION_MOVE

        # A number between -1 and 1, the amount to move in the x-direction.
        self.moveX = 0

        # A number between -1 and 1, the amount to move in the y-direction.
        self.moveY = 0

        # The x-coordinate to shoot at
        self.shootAtX = 0

        # The y-coordinate to shoot at
        self.shootAtY = 0
        #######################################################################

        """ These should never be modified directly.
            You may read them though. """
        #######################################################################
        self.health = self.MAX_HEALTH  # The bot's current health
        self.ammo = self.MAX_AMMO  # The bot's current ammo
        self.mines = self.MAX_MINES  # The bot's current amount of mines
        self.x = 0  # The bot's current x position
        self.y = 0  # The bot's current y position
        self.image = None  # The bot's image

        # These are used to slow down the rate of healing and reloading
        self.reloadtick = 0
        self.healtick = 0

        # Used to calculate accuracy
        self.hits = 0
        self.shots_fired = 0

        self.damage_taken = 0  # Total damage taken
        self.last_hit_by = None  # The last bot to cause damage to this bot
        self.kills = []  # A list containing references to bots killed
        self.killed_by = None  # The bot that killed this bot
        self.zombie_killed = False  # True if killed by an already dead bot
        #######################################################################

        # Append the bot to the list once it's been imported
        arena_globals.bots.append(self)

    def set_name(self, botname):
        if len(botname) > 10:
            botname = botname[0:11]
        self.name = botname

    def set_creator(self, creatorname):
        if len(creatorname) > 15:
            creatorname = creatorname[0:16]
        self.creator = creatorname
