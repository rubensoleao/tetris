import curses

import myCurses
import numpy as np

from game import GameSprite


class GameGrid:
    def __init__(self):
        self.width = 10
        self.height = 24
        self.grid = 0
        self.sprite = None

    def generateGameGrid(self):
        """Creates the empty tetris grid based on objects width and height"""
        self.grid = np.zeros((self.height, self.width))

    def outputGameGrid(self):
        """Prints the game grid to output

        The self.grid represents the tetris game and what is going to be drawn
        The sprites must be drawn to the grid
        """
        for row in range(self.height):
            for column in range(self.width):
                self.printCell(self.grid[row][column])
                # myCurses.stdscr.addstr("0",row,column)
            self.skipGridLine()

    def printCell(self, cellValue):
        """Prints cell based on time"""
        if cellValue == 0:
            myCurses.stdscr.addstr(" ",curses.color_pair(1))
        else:
            myCurses.stdscr.addstr("1")

    def skipGridLine(self):
        """Skips one grid line down"""
        myCurses.stdscr.addstr("\n")

    def draw_sprite(self):
        self.sprite = GameSprite.Sprite()
        self.sprite.set_sprite()
        self.sprite.x = 5
        self.sprite.y= 5
        (sprite_height, sprite_width) = self.sprite.matrix.shape
        for i in range(sprite_height):
            for j in range(sprite_width):
                pixel = self.sprite.matrix[i][j]
                if pixel == 1:
                    x = self.sprite.x + j
                    y = self.sprite.y + i
                    myCurses.stdscr.addstr(y,x," ",curses.color_pair(2))
