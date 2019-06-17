from collections import deque
from typing import List


class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = food
        self.m, self.n = height, width
        self.body = deque([(0, 0)])
        self.score = 0
        self.curr_food = 0
        self.dir_offset = {"U": (-1, 0), "L": (0, -1), "R": (0, 1), "D": (1, 0)}

    def move(self, direction: str) -> int:
        dx, dy = self.dir_offset[direction]
        new_head = self.body[0][0] + dx, self.body[0][1] + dy
        tail = self.body.pop()
        if not self.valid(*new_head): return -1

        self.body.appendleft(new_head)
        if self.curr_food < len(self.food) and new_head == tuple(self.food[self.curr_food]):
            self.body.append(tail) # Add the tail back only if we consume food
            self.curr_food += 1
            self.score += 1

        return self.score

    def valid(self, x, y):
        return 0 <= x <= self.m - 1 and 0 <= y <= self.n - 1 and (x, y) not in self.body



snake = SnakeGame(3, 2, [[1,2],[0,1]])
snake.move('R')
snake.move('D')
snake.move('R')
snake.move('U')
snake.move('L')
snake.move('U')

snake = SnakeGame(3,3,[[2,0],[0,0],[0,2],[2,2]])
snake.move('D')
snake.move('D')
snake.move('R')
snake.move('U')
snake.move('U')
snake.move('L')
snake.move('D')
snake.move('R')
snake.move('R')
snake.move('U')
snake.move('L')
snake.move('D')
