import pygame as py 


# FONT 
py.font.init()
font = py.font.Font(None, 20)

# WINDOW 
window_w, window_h = 720,720
FPS = 60


# player settings 
PLAYER_START_X, PLAYER_START_Y = 400, 400
PLAYER_SPEED = 4

MINE_DELAY = 1000 