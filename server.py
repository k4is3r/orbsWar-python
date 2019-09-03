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


