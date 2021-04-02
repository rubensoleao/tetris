import curses

import time

import myCurses
from game.GameGrid import GameGrid


def gameLoop():
    """Main game loop. Executes the game logic and then updates the visuals"""
    # FPS = 8
    t = 1
    execution_flag = True

    while execution_flag:
        # Executing game loop once every second
        myCurses.stdscr.clear()
        printFrame()

        key = myCurses.stdscr.getch()
        if key > -1:
            key = curses.keyname(key)
            if key in (b"q", b"Q"):
                execution_flag = False

        myCurses.stdscr.addstr(str(t) + "\n----------\n")
        myCurses.stdscr.addstr(str(key))
        curses.flushinp()
        t += 1

        myCurses.stdscr.refresh()
        time.sleep(0.1)


def printFrame():
    # clearFrame()

    # printFrame()
    game_grid.outputGameGrid()
    game_grid.draw_sprite()


myCurses.init()
myCurses.config()

game_grid = GameGrid()
game_grid.generateGameGrid()

# Initialize game grid
try:
    gameLoop()
except Exception as e:
    myCurses.deconfig()

    print("AN ERROR HAS OCCURRED PRESS ANY KEY TO CONTINUE")
    _ = input()

    myCurses.kill()
    myCurses.stdscr = None

    print("Unexpected error:", e)
    raise

if myCurses.stdscr != None:
    myCurses.deconfig()
    myCurses.kill()
