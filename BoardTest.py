import unittest

from Board import Board
from TileType import TileType


class BoardTest(unittest.TestCase):
    def test_something(self):
        schema = [
            [TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.PATH, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE],
            [TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.OBSTACLE, TileType.PATH, TileType.OBSTACLE]
        ]
        board = Board()
        board.initialize()
        for i in range(len(board.tiles)):
            for j in range(len(board.tiles[i])):
                self.assertEqual(board.tiles[i][j].tile_type, schema[i][j])


if __name__ == '__main__':
    unittest.main()
