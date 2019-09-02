import contextlib
with contextlib.redirect_stdout(None): 
    import pygame
#import random
import os

pygame.font.init()


#constantes
PLAYER_RADIUS =10
START_VEL = 9
BALL_RADIUS = 5

W, H = 800, 600

NAME_FONT = pygame.font.SysFont("comicsans", 20)
TIME_FONT = pygame.font.SysFont("comicsans", 30)
SCORE_FONT = pygame.font.SysFont("comicsans",26)

COLORS = [(255,0,0), (255, 128, 0), (255,255,0), (128,255,0),(0,255,0),(0,255,128),(0,255,255),(0, 128, 255), (0,0,255), (0,0,255), (128,0,255),(255,0,255), (255,0,128),(128,128,128), (0,0,0)]

#variables dinamicas 
players = {}
balls = []

#FUNCTIONS
def convert_time(t):
    """
        converts a time given in seconds to a time in 
        minutes 
        param t:int
        return: string
    """
    if type(t) == str:
        return t

    if int(t) <60:
        return str(t) + "s"
    else:
        minutes = str(t // 60)
        seconds = str(t % 60)

        if int(seconds) < 10:
            seconds = "0" + seconds
        return minutes + ":" + seconds


def redraw_window(players, balls, game_time, score):
    """
        draws each frame
        return: None
    """
    pass


if __name__ == '__main__':
    #make window start in top left hand corner
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

    #setup pygame window
    WIN = pygame.display.set_mode((W,H))
    pygame.display.set_caption('Blobs')
    print('Iniciando game')

    pygame.display.flip()

    while True:
        pass