import numpy as np
from random import randint

class Sprite():
    def __init__(self):
        self.matrix = None
        self.x = 0
        self.y = 0

    def set_sprite(self):
        self.matrix = self.getTetrisSprites()


    def getTetrisSprites(self):
        """Defines a dictionary with every sprite in tetris

        Base of the teris object is in y=0
        """

        piece_sprite = [1, 2, 3, 4, 5, 6, 7]
        piece_sprite[0] = np.array([[0, 1, 0], [1, 1, 1]])

        piece_sprite[1] = np.array([[2, 2, 0], [0, 2, 2]])

        piece_sprite[2] = np.array([[0, 3, 3], [3, 3, 0]])

        piece_sprite[3] = np.array([[4, 4], [4, 4]])

        piece_sprite[4] = np.array([[5, 0], [5, 0], [5, 5]])

        piece_sprite[5] = np.array([[0, 6], [0, 6], [6, 6]])

        piece_sprite[6] = np.array([[7], [7], [7], [7]])

        return piece_sprite[randint(0,6)]
