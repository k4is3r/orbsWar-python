import socket
from _thread import *
import _pickle as pickle
import time
import random
import math

# setup sockets
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#set constants

PORT = 5555

BALL_RADIUS = 5
START_RADIUS = 7

ROUND_TIME = 60 * 8

MASS_LOSS_TIME = 7

#setting with and height 

W, H = 800,600

HOST_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(HOST_NAME)

# try to connect to server
try:
    S.bind((SERVER_IP, PORT))
except socket.error as e:
    print(str(e))
    print("[SERVER] Server could not start")
    quit()
#listen for connections
S.listen()
print(f"[SERVER] Server Started with local ip {SERVER_IP}")

#dynamic variables
players = {}
balls = []
connections = 0
_id = 0
colors = [
            (255,0,0), (255, 128, 0), (255,255,0),
            (128,255,0),(0,255,0),(0,255,128),
            (0,255,255),(0, 128, 255), (0,0,255),
            (0,0,255), (128,0,255),(255,0,255),
            (255,0,128),(128,128,128), (0,0,0)
        ]
start = False
stat_time = 0
game_time = "Starting Soon"
nxt = 1

#Functions
def release_mass(players):
    """
    releases the mass of players
    players: dict
    return: None
    """
    for player in players:
        p = players[player]
        if p["score"] > 8:
            p["score"] = math.floor(p["score"] * 0.95)

def check_collision(players, balls):
    """
    checks if any of the player have collied with any of the balls
    players: a dictonary of players
    ball: a list of balls
    return: None
    """
    to_delete =  []
    for player in players:
        p = players[player]
        x = p["x"]
        y = p["y"]
        for ball in balls:
            bx = ball[0]
            by = ball[1]

            dis = math.sqrt((x - bx)**2 + (y-by)**2)
            if dis <= START_RADIUS + p["score"]:
                p["score"] = p["score"] + 0.5
                balls.remove(ball)
