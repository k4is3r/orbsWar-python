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
