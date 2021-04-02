import os
import sys
import time

import myCurses
from game.GameGrid import GameGrid


def gameLoop():
    """Main game loop. Executes the game logic and then updates the visuals"""
    # FPS = 8
    while True:
        # Executing game loop once every second
        myCurses.stdscr.clear()
        printFrame()
        time.sleep(1)


def printFrame():
    # clearFrame()

    # printFrame()
    game_grid.outputGameGrid()
    game_grid.draw_sprite()


#
# Main
#
myCurses.init()

game_grid = GameGrid()
game_grid.generateGameGrid()

# stdcr MUST BE GLOBAL

myCurses.config()
myCurses.deconfig()

# Initialize game grid
try:
    gameLoop()
except Exception as e:
    myCurses.deconfig()

    print("AN ERROR HAS OCCURRED PRESS ANY KEY TO CONTINUE")
    _ = input()

    myCurses.kill()

    print("Unexpected error:", e)
    raise
