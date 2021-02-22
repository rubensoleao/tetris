import os
import time
import numpy as np

class GameGrid:

    def __init__(self):
        self.width=10
        self.height=24
        self.grid=0

    def generateGameGrid(self):
        '''Creates the empty tetris grid based on objects width and height'''
        self.grid = np.zeros((self.height,self.width))

    def printGameGrid(self):
        '''Prints the game grid to output'''
        for row in range(self.height):
            for column in range(self.width):
                self.printCell(self.grid[row][column])
            self.skipGridLine()


    def printCell(self, cellValue):
        '''Prints cell based on time'''
        if cellValue==0:
            self.printEmptyCell()


    def printEmptyCell(self):
        '''prints an empty cell'''
        print('0', end='')

    
    def skipGridLine(self):
        '''Skips one grid line down'''
        print()


class Spirte():
    ''' Sprites are a colection of vectors in 2d space '''

    def __init__():
        coordinates = []


# class Pixel():
#     ''' Define a  '''

def gameLoop():
    '''Main game loop. Executes the game logic and then updates the visuals'''
    #FPS = 8
        
    while True:
        #Executing game loop once every second

        printFrame()

        time.sleep(1)


def printFrame():
    #clearFrame()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #printFrame()
    game_grid.printGameGrid()


#Initialize game grid
game_grid = GameGrid()
game_grid.generateGameGrid()


gameLoop()