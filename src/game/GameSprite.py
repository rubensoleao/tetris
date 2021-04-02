
import numpy as np

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
