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
        self.grid = np.zeros((self.height, self.width), int)

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

        if self.sprite_collided(self.sprite):
            self.sprite.x += change * -1

    def rotate_sprite(self, direction):
        positionedSprite = GameSprite.Sprite()
        positionedSprite.matrix = self.sprite.matrix
        positionedSprite.x = self.sprite.x
        positionedSprite.y = self.sprite.y
        if direction == "couterclock":
            positionedSprite.matrix = np.rot90(positionedSprite.matrix, k=3)
        elif direction == "clockwise":
            positionedSprite.matrix = np.rot90(positionedSprite.matrix, k=1)
        else:
            return
        (_, sprite_width) = positionedSprite.matrix.shape

        positionOverflow = positionedSprite.x + sprite_width - self.width
        if positionOverflow> 0:
            new_sprite_x  = positionedSprite.x - positionOverflow

            if new_sprite_x < 0:
                return
            else:
                positionedSprite.x = new_sprite_x

        if self.sprite_collided(positionedSprite) == False:
            self.sprite.matrix = positionedSprite.matrix
            self.sprite.x = positionedSprite.x

    def gravity(self):
        self.sprite.y = self.sprite.y + 1
        if self.sprite_collided(self.sprite):
            self.sprite.y -= 1
            x = self.sprite.x
            y = self.sprite.y
            (sprite_height, sprite_width) = self.sprite.matrix.shape

            self.grid[y : y + sprite_height, x : x + sprite_width] += self.sprite.matrix

            # Delete and create new Sprite
            del self.sprite
            self.sprite = GameSprite.Sprite()
            self.sprite.set_sprite()
            self.line_finish()

    def sprite_collided(self, sprite):
        try:
            x = sprite.x
            y = sprite.y
            (sprite_height, sprite_width) = sprite.matrix.shape
            aux_matrix = self.grid[y : y + sprite_height, x : x + sprite_width]
            if aux_matrix.shape != sprite.matrix.shape:
                return True
            summed_matrix = aux_matrix + sprite.matrix
            if summed_matrix.max() > 1:
                return True
            return False  # No colision
        except Exception:
            return True

    def line_finish(self):
        empty_line = np.zeros((1,self.width),int) 
        supMatrix = np.empty((0, self.width), int)
        for i in range(self.height):
            line = self.grid[i,:][None,:]
            if 0 in line:
                supMatrix = np.append(supMatrix, line, axis = 0)
            else:
                supMatrix = np.append(empty_line,supMatrix, axis = 0)
        self.grid = supMatrix
