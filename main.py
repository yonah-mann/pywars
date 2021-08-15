###############################################################################
#                                                                             #
# The main PyWars file. No code in here should be modified, except adding #
# more bot file imports.                                                      #
#                                                                             #
###############################################################################

import pygame
import pygame.locals
import sys
import arena_globals
import bullet
import mine


# All bots are imported here. To add your bot, add 'import bots.bot_file_name'.
# The order in which bots are imported determines their starting positions.
# Do not import any more or any less than four bots. I have yet to write code
# to handle this.
###############################################################################
import bots.Daedalus
import bots.Denton
import bots.Page
import bots.Icarus
###############################################################################

# Image locations
ICON_FILE = 'images/icon.jpg'
BG_FILE = 'images/arena.jpg'
BULLET_IMG_FILE = 'images/bullet.jpg'
MINE_IMG_FILE = 'images/mine.png'
PANEL_IMG_FILE = 'images/char_panel.jpg'
SKULL_IMG_FILE = 'images/skull.jpg'
EXPLOSION_IMG_FILE = 'images/explosion.jpg'

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Sizes and dimensions
TAUNT_SIZE = 16
MINE_SIZE = 25
PANEL_SIZE = 200
BULLET_SIZE = 5
BOT_SIZE = 50

# Program properties
SCREEN_TITLE = 'PyWars'
FPS = 30

# Miscellaneous
BOT_START_OFFSET = 10
BOT_IMG_EXT = '.jpg'
BULLET_DAMAGE = 5
TAUNT_COLOR = COLOR_WHITE


# Mundane functions
def set_icon(icon_file):
    # If there is no icon to load, don't worry about it
    try:
        pygame.display.set_icon(pygame.image.load(icon_file))
    except:
        print('Icon could not be loaded!')


def load_image(filename):
    img = pygame.image.load(filename)
    img.convert()
    return img


def create_window(width, height, title, icon=None):
    # Lower the buffer size to remove sound lag if I decide to include music
    # pygame.mixer.pre_init(buffer=512)
    pygame.init()
    set_icon(icon)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen


def quit_arena():
    pygame.quit()
    sys.exit()


def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            quit_arena()


# Functions pertaining to bullets
def fire_bullet(bot, bot_x, bot_y, targetX, targetY):
    # Only one line, but I may want to add more functionality in the future
    bullet.Bullet(bot, bot_x, bot_y, targetX, targetY)


def process_bullets():
    for bullet in arena_globals.bullets:
        bullet.move()

        # If bullet goes out of bounds, remove it
        if (bullet.x > arena_globals.ARENA_END_X or bullet.x < arena_globals.ARENA_START_X or
                bullet.y > arena_globals.ARENA_END_Y or bullet.y < arena_globals.ARENA_START_Y):
            arena_globals.bullets.remove(bullet)

        # Check for collission with bot. If so, damage bot and remove bullet.
        for bot in arena_globals.bots:
            # Don't want bots being damaged by their own bullets
            if bot is not bullet.owner_bot:
                bullet_rect = pygame.Rect(bullet.x, bullet.y,
                                          BULLET_SIZE, BULLET_SIZE)
                bot_rect = pygame.Rect(bot.x, bot.y, BOT_SIZE, BOT_SIZE)
                if bot_rect.colliderect(bullet_rect):
                    bot.health -= BULLET_DAMAGE
                    bot.damage_taken += BULLET_DAMAGE
                    bot.last_hit_by = bullet.owner_bot
                    bullet.owner_bot.hits += 1
                    if bullet in arena_globals.bullets:
                        arena_globals.bullets.remove(bullet)


def draw_bullets():
    for bullet in arena_globals.bullets:
        screen.fill(COLOR_BLACK, pygame.Rect(bullet.x, bullet.y,
                    BULLET_SIZE, BULLET_SIZE))


# Functions pertaining to bots
def bot_move(bot):
    # Stop the bot from moving too fast
    if bot.moveX < -1:
        bot.moveX = -1
    elif bot.moveX > 1:
        bot.moveX = 1
    if bot.moveY < -1:
        bot.moveY = -1
    elif bot.moveY > 1:
        bot.moveY = 1

    # Let the bot move in the right direction
    bot.x += bot.moveX * bot.MOVE_SPEED
    bot.y += bot.moveY * bot.MOVE_SPEED

    # Stop the bot from moving out of bounds
    if bot.x + (bot.moveX * bot.MOVE_SPEED) < arena_globals.ARENA_START_X:
        bot.x = arena_globals.ARENA_START_X
    elif bot.x + (bot.moveX * bot.MOVE_SPEED) + BOT_SIZE > arena_globals.ARENA_END_X:
        bot.x = arena_globals.ARENA_END_X - BOT_SIZE
    if bot.y + (bot.moveY * bot.MOVE_SPEED) < arena_globals.ARENA_START_Y:
        bot.y = arena_globals.ARENA_START_Y
    elif bot.y + (bot.moveY * bot.MOVE_SPEED) + BOT_SIZE > arena_globals.ARENA_END_Y:
        bot.y = arena_globals.ARENA_END_Y - BOT_SIZE


def bot_shoot(bot):
    if bot.ammo >= 1:
        bot.ammo -= 1
        startx = bot.x + (BOT_SIZE / 2)
        starty = bot.y + (BOT_SIZE / 2)
        fire_bullet(bot, startx, starty, bot.shootAtX, bot.shootAtY)
        bot.shots_fired += 1


def bot_heal(bot):
    # Used so the bot only heals every other frame
    bot.healtick += 1
    if bot.health < bot.MAX_HEALTH and (bot.healtick % 2):
        bot.health += 1


def bot_reload(bot):
    # Used so the bot only reloads every other frame
    bot.reloadtick += 1
    if bot.ammo < bot.MAX_AMMO and (bot.reloadtick % 2):
        bot.ammo += 1


def bot_place_mine(bot):
    if bot.mines >= 1:
        mineX = bot.x + (BOT_SIZE / 2) - (MINE_SIZE / 2)
        mineY = bot.y + (BOT_SIZE / 2) - (MINE_SIZE / 2)
        mine.Mine(bot, mineX, mineY)
        bot.mines -= 1


def pick_action(bot):
    """ Decide which function to execute based on bot's chosen action. """
    if bot.action == bot.ACTION_MOVE:
        bot_move(bot)
    elif bot.action == bot.ACTION_SHOOT:
        bot_shoot(bot)
    elif bot.action == bot.ACTION_HEAL:
        bot_heal(bot)
    elif bot.action == bot.ACTION_RELOAD:
        bot_reload(bot)
    elif bot.action == bot.ACTION_MINE:
        bot_place_mine(bot)


def check_mine_detonation(bot):
    """ Check if a bot stepped on a mine, and if so, detonate it. """
    for mine in arena_globals.mines:
        # Don't want bot detonating its own mine
        if bot is not mine.owner_bot:
            mine_rect = pygame.Rect(mine.x, mine.y, MINE_SIZE, MINE_SIZE)
            bot_rect = pygame.Rect(bot.x, bot.y, BOT_SIZE, BOT_SIZE)
            if bot_rect.colliderect(mine_rect):
                mine.detonate(MINE_SIZE, BOT_SIZE)


def bot_check_death(bot):
    """ Performs all actions necessary upon a bot's unfortunate demise. """
    if bot.health <= 0:
        bot.killed_by = bot.last_hit_by
        bot.last_hit_by.kills.append(bot)
        arena_globals.bots.remove(bot)
        # Use insert instead of append to show placing (1st, 2nd, 3rd, 4th)
        arena_globals.dead_bots.insert(0, bot)
        bot.image = skull_img
        # Check if the bot that killed this bot is dead as well
        if bot.killed_by.killed_by is not None:
            bot.zombie_killed = True


def process_bots():
    """ Loops through all bots and performs the action each bot chose. """
    # If last bot standing, perform victory dance!
    if len(arena_globals.bots) == 1:
        arena_globals.bots[0].victory_dance()
        return

    for bot in arena_globals.bots:
        bot.do_action()
        pick_action(bot)
        check_mine_detonation(bot)
        bot_check_death(bot)


def position_bots():
    """ Puts the four bots in their starting positions.
        Should probably put this in some sorta loop. Oh well."""
    arena_globals.bots[0].x = arena_globals.ARENA_START_X + BOT_START_OFFSET
    arena_globals.bots[0].y = arena_globals.ARENA_START_Y + BOT_START_OFFSET

    arena_globals.bots[1].x = arena_globals.ARENA_END_X - BOT_START_OFFSET - BOT_SIZE
    arena_globals.bots[1].y = arena_globals.ARENA_START_Y + BOT_START_OFFSET

    arena_globals.bots[2].x = arena_globals.ARENA_START_X + BOT_START_OFFSET
    arena_globals.bots[2].y = arena_globals.ARENA_END_Y - BOT_START_OFFSET - BOT_SIZE

    arena_globals.bots[3].x = arena_globals.ARENA_END_X - BOT_START_OFFSET - BOT_SIZE
    arena_globals.bots[3].y = arena_globals.ARENA_END_Y - BOT_START_OFFSET - BOT_SIZE


def load_bot_images():
    for bot in arena_globals.bots:
        bot.image = load_image('bots/images/' + bot.name + BOT_IMG_EXT)


def draw_bots():
    for bot in arena_globals.bots:
        screen.blit(bot.image, (bot.x, bot.y))


def draw_bot_taunts():
    """ NEEDS WORK! Magic numbers!"""
    for bot in arena_globals.bots:
        if bot.x > (arena_globals.ARENA_END_X - 100):
            xpos = bot.x - (7 * len(bot.taunt))
        else:
            xpos = bot.x + BOT_SIZE + 10
        ypos = bot.y + (BOT_SIZE / 2) - 10
        draw_text_label(bot.taunt, TAUNT_SIZE, TAUNT_COLOR, (xpos, ypos))


# Functions pertaining to mines
def draw_mines():
    for mine in arena_globals.mines:
        screen.blit(mine_img, (mine.x, mine.y))


# Miscellaneous functions
def draw_text_label(text_value, font_size, font_color,
                    position, font_type=None):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(text_value, True, font_color)
    text_rect = text.get_rect(topleft=position)
    screen.blit(text, text_rect)


def draw_char_panel(bot, ypos):
    """ Draws a character panel with all stats. NEEDS WORK! MAGIC NUMBERS!
        Fine for now though, will change if I get prettier panels. """
    screen.blit(panel_img, (0, ypos))
    screen.blit(bot.image, (7, ypos + 10))
    draw_text_label(bot.name, 28, COLOR_WHITE, (70, ypos + 20))
    draw_text_label(bot.creator, 16, COLOR_WHITE, (70, ypos + 40))

    # If bot is dead, show a simplified panel
    if bot.killed_by is not None:
        draw_text_label('Killed by ' + str(bot.killed_by.name),
                        24, COLOR_WHITE, (30, ypos + 110))
        if bot.zombie_killed:
            draw_text_label('...from the grave!',
                            24, COLOR_WHITE, (30, ypos + 130))
        return

    draw_text_label('Health: ' + str(bot.health),
                    24, COLOR_WHITE, (10, ypos + 70))
    draw_text_label('Ammo: ' + str(bot.ammo),
                    24, COLOR_WHITE, (10, ypos + 90))
    draw_text_label('Mines: ' + str(bot.mines),
                    24, COLOR_WHITE, (10, ypos + 110))
    draw_text_label('Kills: ' + str(len(bot.kills)),
                    24, COLOR_WHITE, (10, ypos + 130))

    # Calculate accuracy
    if bot.shots_fired == 0:
        accuracy = 100
    else:
        accuracy = int(round((bot.hits /
                           float(bot.shots_fired)) * 100))

    draw_text_label('Accuracy: ' + str(accuracy) + '%',
                    24, COLOR_WHITE, (10, ypos + 150))

    if bot.action == bot.ACTION_MOVE:
        action = 'Moving to position!'
    elif bot.action == bot.ACTION_SHOOT:
        action = 'Firing round!'
    elif bot.action == bot.ACTION_HEAL:
        action = 'Healing damage!'
    elif bot.action == bot.ACTION_RELOAD:
        action = 'Reloading!'
    elif bot.action == bot.ACTION_MINE:
        action = 'Placing mine!'
    else:
        action = 'Lollygagging...'

    draw_text_label(action, 24, COLOR_WHITE, (10, ypos + 170))


def draw_char_panels():
    """ Draws all four character panels. """
    for i, bot in enumerate(arena_globals.bots + arena_globals.dead_bots):
        draw_char_panel(bot, i * PANEL_SIZE)


def draw_explosions():
    for expl in arena_globals.explosions:
        screen.blit(explosion_img, (expl['x'], expl['y']))


def process_explosions():
    """ Removes the explosion image after half a second. """
    for expl in arena_globals.explosions:
        expl['count'] += 1
        if expl['count'] >= FPS / 2:
            arena_globals.explosions.remove(expl)


# Initialize some stuff
screen = create_window(arena_globals.SCREEN_WIDTH, arena_globals.SCREEN_HEIGHT, SCREEN_TITLE, ICON_FILE)
fps_clock = pygame.time.Clock()
position_bots()

# Load images
load_bot_images()
arena_bg = load_image(BG_FILE)
mine_img = load_image(MINE_IMG_FILE)
panel_img = load_image(PANEL_IMG_FILE)
skull_img = load_image(SKULL_IMG_FILE)  # Represents dead bots
explosion_img = load_image(EXPLOSION_IMG_FILE)


# Main Loop
while 1:
    # Set the title which also displays the FPS
    pygame.display.set_caption(SCREEN_TITLE + ' - FPS: ' +
                               str(round(fps_clock.get_fps(), 1)))

    handle_input()
    process_bots()
    process_bullets()
    process_explosions()

    # Clear screen and draw background
    screen.fill(COLOR_BLACK)
    screen.blit(arena_bg, (arena_globals.STATS_BAR_W, 0))

    draw_char_panels()
    draw_mines()
    draw_bullets()
    draw_bots()
    draw_bot_taunts()
    draw_explosions()

    pygame.display.flip()

    fps_clock.tick(FPS)
