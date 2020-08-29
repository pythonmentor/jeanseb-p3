from Board import Board
from Direction import Direction
from Personage import Personage
from Position import Position
import pygame
from pygame.locals import *

from TileType import TileType


class Game:
    def __init__(self):
        self.boards = []
        self.personage = Personage(Position(13, 14))
        self.level = 0

    def initialize(self):
        board = Board()
        board.initialize()
        self.boards.append(board)
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Pygame Keyboard Test')
        pygame.mouse.set_visible(0)

    @property
    def next_tile(self):
        next_x = self.personage.next_position.x
        next_y = self.personage.next_position.y
        return self.boards[self.level].tiles[next_y][next_x]

    def launch(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.personage.direction = Direction.UP
                    elif event.key == K_DOWN:
                        self.personage.direction = Direction.DOWN
                    elif event.key == K_RIGHT:
                        self.personage.direction = Direction.RIGHT
                    elif event.key == K_LEFT:
                        self.personage.direction = Direction.LEFT
                    if self.next_tile.tile_type == TileType.PATH:
                        self.personage.move(self.personage.next_position)
                        print('JE ME DEPLACE VERS {}'.format(self.personage.direction))
                    else:
                        print('IL Y A UN MUR VERS {}'.format(self.personage.direction))
