import math
#from map import *
from mapconstants import *

scroll = [10,10]

FOV = 60 * (math.pi / 180)

RES = 60

WINDOW_WIDTH = COLS * TILESIZE
WINDOW_HEIGHT = ROWS * TILESIZE
#WINDOW_WIDTH = 5000
#WINDOW_HEIGHT = 6000

NUM_RAYS = WINDOW_WIDTH // RES