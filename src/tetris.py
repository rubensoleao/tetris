import curses

import time

import myCurses
from game.GameGrid import GameGrid

t = None
execution_flag = None
def gameLoop():
    """Main game loop. Executes the game logic and then updates the visuals"""
    # FPS = 8
    global t 
    global execution_flag 
    
    t = 1
    execution_flag = True
    while execution_flag:
        # Executing game loop once every second
        myCurses.stdscr.clear()
        printFrame()
        handle_input()

        t += 1

        myCurses.stdscr.refresh()
        time.sleep(0.1)


def printFrame():
    # clearFrame()

    # printFrame()
    game_grid.outputGameGrid()
    if t%2 == 0:
        game_grid.gravity()
    game_grid.draw_sprite()

def handle_input():
    global execution_flag
    key = myCurses.stdscr.getch()
    
    if key == -1:
        return
    
    key = curses.keyname(key)
    if key in (b"q", b"Q"):
        execution_flag = False
    if key == b"KEY_LEFT":
        game_grid.move_sprite('left')
    elif key == b"KEY_RIGHT":
        game_grid.move_sprite('right')
    elif key == b"KEY_UP":
        game_grid.rotate_sprite('couterclock')
    elif key == b"KEY_DOWN":
        game_grid.rotate_sprite('clockwise')
    
    curses.flushinp()






myCurses.init()
myCurses.config()

game_grid = GameGrid()
game_grid.generateGameGrid()
game_grid.add_sprite()
# Initialize game grid
try:
    gameLoop()
except Exception as e:
    myCurses.deconfig()

    print("AN ERROR HAS OCCURRED PRESS ENTER TO CONTINUE")
    _ = input()

    myCurses.kill()
    myCurses.stdscr = None

    print("Unexpected error:", e)
    raise

if myCurses.stdscr != None:
    myCurses.deconfig()
    myCurses.kill()
