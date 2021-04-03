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
            myCurses.stdscr.addstr(" ", curses.color_pair(1))
        else:
            myCurses.stdscr.addstr("1")

    def skipGridLine(self):
        """Skips one grid line down"""
        myCurses.stdscr.addstr("\n")

    def add_sprite(self, x=3, y=0):
        self.sprite = GameSprite.Sprite()
        self.sprite.set_sprite()
        self.sprite.x = x
        self.sprite.y = y

    def draw_sprite(self):
        (sprite_height, sprite_width) = self.sprite.matrix.shape
        for i in range(sprite_height):
            for j in range(sprite_width):
                pixel = self.sprite.matrix[i][j]
                if pixel == 1:
                    x = self.sprite.x + j
                    y = self.sprite.y + i
                    myCurses.stdscr.addstr(y, x, " ", curses.color_pair(2))

    def move_sprite(self, direction):
        # Should move sprite moving inside sprite class
        if direction == "left":
            change = -1
            self.sprite.x -= 1
        elif direction == "right":
            change = 1
            self.sprite.x += 1

        if self.sprite_collided():
            self.sprite.x += change * -1

    def gravity(self):
        self.sprite.y = self.sprite.y + 1
        if self.sprite_collided():
            self.sprite.y -= 1
            x = self.sprite.x
            y = self.sprite.y
            (sprite_height, sprite_width) = self.sprite.matrix.shape

            self.grid[y : y + sprite_height, x : x + sprite_width] += self.sprite.matrix

            # Delete and create new Sprite
            del self.sprite
            self.sprite = GameSprite.Sprite()
            self.sprite.set_sprite()

    def sprite_collided(self):
        try:
            x = self.sprite.x
            y = self.sprite.y
            (sprite_height, sprite_width) = self.sprite.matrix.shape
            aux_matrix = self.grid[y : y + sprite_height, x : x + sprite_width]
            if aux_matrix.shape != self.sprite.matrix.shape:
                return True
            summed_matrix = aux_matrix + self.sprite.matrix
            if summed_matrix.max() > 1:
                raise Exception
            return False  # No colision
        except Exception:
            return True