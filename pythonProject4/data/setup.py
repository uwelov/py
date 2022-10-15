import os
import pygame as pg
from data import tools
from data import constants as c

GAME = 'LET THE GAME BEGIN'
ORIGINAL_CAPTION = 'Fantasy RPG'
pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP,pg.QUIT])
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode((c.WIDTH, c.HEIGHT))
SCREEN_RECT = SCREEN.get_rect()
PATH = os.path.dirname(os.path.dirname(__file__))
FONTS = tools.load_all_fonts(os.path.join(PATH, 'resources', 'fonts'))
MUSIC = tools.load_all_music(os.path.join(PATH, 'resources', 'music'))
GFX = tools.load_all_gfx(os.path.join(PATH, 'resources', 'graphics'))
SFX = tools.load_all_sfx(os.path.join(PATH, 'resources', 'sound'))
TMX = tools.load_all_tmx(os.path.join(PATH, 'resources', 'tmxmap'))
FONT = pg.font.Font(FONTS[c.MAIN_FONT], 20)