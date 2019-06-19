import operator

from copy import deepcopy
from typing import List
from functools import reduce

from dataclasses import dataclass, field

from player import Player


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Board:
    board: List[int] = field(default_factory=lambda: [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def move_new(self, position: Position, player: Player):
        newBoard = deepcopy(self.board)
        newBoard[position.x][position.y] = player.player

        return newBoard

    def move(self, position: Position, player: Player):
        self.board[position.x][position.y] = player.player

    def print(self):
        for row in self.board:
            for col in row:
                print(str(col), end=' ')
            print()

    def full(self):
        return not any(map(lambda x: x == 0, reduce(operator.iconcat, self.board, [])))

    def empty_positions(self):
        positions = []

        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    positions.append(Position(row, col))

        return positions

    def status(self):
        # rows
        for i in range(3):
            if self.board[i][0] != 0 and self.board[i][1] != 0\
                and self.board[i][2] != 0 and self.board[i][0] == self.board[i][1]\
                    and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]

        # cols
        transposed = Board()

        for i in range(3):
            for j in range(3):
                transposed.board[i][j] = self.board[j][i]

        for i in range(3):
            if transposed.board[i][0] != 0 and transposed.board[i][1] != 0\
                and transposed.board[i][2] != 0 and transposed.board[i][0] == transposed.board[i][1]\
                    and transposed.board[i][1] == transposed.board[i][2]:
                return transposed.board[i][0]

        # prim diag
        if self.board[0][0] != 0 and self.board[1][1] != 0\
            and self.board[2][2] != 0 and self.board[0][0] == self.board[1][1]\
                and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        # secondary diag
        if self.board[0][2] != 0 and self.board[1][1] != 0\
            and self.board[2][0] != 0 and self.board[0][2] == self.board[1][1]\
                and self.board[2][0] == self.board[1][1]:
            return self.board[0][2]

        # draw
        if self.full():
            return 3

        # in progress
        return -1
