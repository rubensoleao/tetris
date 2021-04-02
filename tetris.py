import os
import time
import numpy as np
import sys
import curses
#
# GRID
#


event=0
class GameGrid:

    def __init__(self):
        self.width=10
        self.height=24
        self.grid=0
        self.sprite_list = []

    def generateGameGrid(self):
        '''Creates the empty tetris grid based on objects width and height'''
        self.grid = np.zeros((self.height,self.width))

    def outputGameGrid(self):
        '''Prints the game grid to output

            
            The self.grid represents the tetris game and what is going to be drawn
            The sprites must be drawn to the grid
        '''
        for row in range(self.height):
            for column in range(self.width):
                self.printCell(self.grid[row][column])
                # stdscr.addstr("0",row,column)
            self.skipGridLine()
        stdscr.refresh()


    def printCell(self, cellValue):
        '''Prints cell based on time'''
        if cellValue==0:
            stdscr.addstr("0")
        else:
            stdscr.addstr("1")
    
    def skipGridLine(self):
        '''Skips one grid line down'''
        stdscr.addstr("\n")


    def draw_sprite(self):
        sprite = getTetrisSprites()
        x = 5
        y = 5
        (sprite_height, sprite_width) = sprite.shape
        self.grid[x:x+sprite_height, y:y+sprite_width] = sprite

#
# SPRITES
#

def Sprite():
    
    def __init__(self):
        self.matrix = np.array()
        self.x = 0
        self.y = 0 

def getTetrisSprites():
    ''' Defines a dictionary with every sprite in tetris  

        Base of the teris object is in y=0
    '''

    piece_sprite =[1,2,3,4,5,6,7]
    piece_sprite[0] = np.array([[0,1,0],
                                [1,1,1]])  #xxx

    piece_sprite[1] = np.array([[1,1,0],
                                [0,1,1]])  

    piece_sprite[2] = np.array([[0,1,1],
                                [1,1,0]])  

    piece_sprite[3] = np.array([[1,1],
                                [1,1]])  
    
    piece_sprite[4] = np.array([[1,0],
                                [1,0],
                                [1,1]])

    piece_sprite[5] = np.array([[0,1],
                                [0,1],
                                [1,1]])

    piece_sprite[6] = np.array([[1],
                                [1],
                                [1],
                                [1]])                

    return piece_sprite[0]
#
# Draw
#


#
#   GAME, LOOP Frames
#

def gameLoop():
    '''Main game loop. Executes the game logic and then updates the visuals'''
    # FPS = 8
    while True:
        # Executing game loop once every second
        stdscr.clear()
        printFrame()
        time.sleep(1)

def printFrame():
    #clearFrame()

    #printFrame()
    game_grid.outputGameGrid()
    game_grid.draw_sprite()

#
#   curses
#


def init_curses():
    return curses.initscr()

def config_curses():
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

def deconfig_curses():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()

def kill_curses():
    curses.endwin()

#
# Main
#

game_grid = GameGrid()
game_grid.generateGameGrid()

#stdcr MUST BE GLOBAL
stdscr = init_curses()
config_curses()
deconfig_curses()

#Initialize game grid
try:
    gameLoop()
except Exception as e:
    deconfig_curses()

    print("AN ERROR HAS OCCURRED PRESS ANY KEY TO CONTINUE")
    _ =input()

    kill_curses()
    
    print("Unexpected error:", e)
    raise