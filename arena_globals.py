# This file just contains lists holding all important objects in the arena.
# You will need to access these frequently, but of course, no modifying.

# Dimensions of the arena
STATS_BAR_W = 200
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = SCREEN_WIDTH - STATS_BAR_W
ARENA_START_X = STATS_BAR_W
ARENA_END_X = SCREEN_WIDTH
ARENA_START_Y = 0
ARENA_END_Y = SCREEN_HEIGHT
GRID_SIZE = 50
MAX_TURNS = 1000

# List containing instances of all living bots.
bots = []

# List containing all dead bots.
# You probably won't really need this, its use is more internal.
dead_bots = []

# List containing all bullets.
bullets = []

# List containing all placed mines.
mines = []

# List containing all explosions (which is a dictionary).
# Another list you probably won't use.
explosions = []
