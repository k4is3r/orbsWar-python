import contextlib
with contextlib.redirect_stdout(None): 
    import pygame

import random
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
    # fill screen white, to clear old frames
    WIN.fill((255,255,255))
    # draw all the orbs
    for ball in balls:
        pygame.draw.circle(WIN, ball[2], (ball[0], ball[1]), BALL_RADIUS)
    # draw each player in the list
    for player in sorted(players, key=lambda x: players[x]["score"]):
        p = players[player]
        pygame.draw.circle(WIN, p["color"], (p["x"], p["y"]), PLAYER_RADIUS + round(p["score"]))
        # render and draw name for each player
        text = NAME_FONT.render(p["name"], 1, (0,0,0))
        WIN.blit(text, (p["x"] - text.get_width()/2, p["y"] - text.get_height()/2))

    # draw scoreboard
    sort_players = list(reversed(sorted(players, key= lambda x: players[x]["score"])))
    title = TIME_FONT.render("Puntation Table", 1, (0,0,0))
    start_y = 25
    x = W - title.get_width() - 10
    WIN.blit(title, (x,5))

    ran = min(len(players), 3)
    for count, i in enumerate(sort_players[:ran]):
        text = SCORE_FONT.render(str(count+1) + "." + str(players[i]["name"]), 1, (0,0,0))
        WIN.blit(text, (x, start_y + count * 20))

    # draw time
    text = TIME_FONT.render("Time: " + convert_time(game_time), 1, (0,0,0,))
    WIN.blit(text, (10,10))

    #draw score
    text = TIME_FONT.render("Puntuation: " + str(round(score)), 1, (0,0,0))
    WIN.blit(text, (10,15 + text.getheight()))




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