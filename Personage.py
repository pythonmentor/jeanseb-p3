from Direction import Direction
from Position import Position


class Personage:
    def __init__(self, position, direction=None):
        self.direction = direction
        self.position = position

    def move(self, position):
        self.position = position

    @property
    def next_position(self):
        next_x = self.position.x
        next_y = self.position.y
        if self.direction == Direction.UP:
            next_y -= 1
        elif self.direction == Direction.RIGHT:
            next_x += 1
        elif self.direction == Direction.DOWN:
            next_y += 1
        elif self.direction == Direction.LEFT:
            next_x -= 1
        return Position(next_x, next_y)
