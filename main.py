#!/usr/bin/env python3
import random
import datetime
import os
import time
import json


###### CONFIGS ######
plane = []
SIZE = (230, 59)
OUTPUT = True
rarity = 10
refresh_rate = 1/3
#####################


dead = 0
alive = 0
generation = 0

for y in range(0, SIZE[1]):
    line = []
    for x in range(0, SIZE[0]):
        line.append(random.randint(0, rarity) == 0)
    plane.append(line)

def draw():
    os.system("clear")
    for line in plane:
        for elem in line:
            if elem == 1:
                print("X", end="")
            else:
                print(".", end="")
        print()
    if OUTPUT:
        with open("generations.txt", 'a') as file:
            for line in plane:
                for elem in line:
                    if elem == 1:
                        file.write("X")
                    else:
                        file.write(".")
                file.write("\n")
            file.write("\n")


def drawStatistics():
    print("-"*SIZE[0])
    print("SIZE=({}, {}), GENERATION={}, DEAD={}, ALIVE={}".format(SIZE[0], SIZE[1], generation, dead, alive))
    print("-"*SIZE[0])
    if OUTPUT:
        with open("generations.txt", 'a') as file:
            file.write(str("-"*SIZE[0]) + "\n")
            file.write("SIZE=({}, {}), GENERATION={}, DEAD={}, ALIVE={}".format(SIZE[0], SIZE[1], generation, dead, alive) + "\n")
            file.write(str("-"*SIZE[0]) + "\n")
            file.write("\n\n\n")

def countNeightbours(coord: tuple):
    global plane
    state = plane[coord[1]][coord[0]]
    new_state = state
    total_alive = 0
    for y in range(coord[1]-1, coord[1]+2):
        for x in range(coord[0]-1, coord[0]+2):
            if (x > 0 and x < SIZE[0]-1) and (y > 0 and y < SIZE[1]-1) and plane[y][x] == 1 and (x, y) != coord:
                total_alive += 1
    if state == 0:
        if total_alive != 3:
            new_state = 0
        else:
            new_state = 1
    else:
        if total_alive > 3 or total_alive < 2:
            new_state = 0
        else:
            new_state = 1
    return new_state

def logic():
    global dead
    global alive
    global plane
    dead = 0
    alive = 0
    for line in plane:
        for elem in line:
            if elem == 0:
                dead += 1
            else:
                alive += 1
    new_plane = []
    for y in range(0, SIZE[1]):
        new_line = []
        for x in range(0, SIZE[0]):
            new_line.append(countNeightbours((x, y)))
        new_plane.append(new_line)
    plane = new_plane

while True:
    draw()
    logic()
    drawStatistics()
    generation += 1
    time.sleep(refresh_rate)
