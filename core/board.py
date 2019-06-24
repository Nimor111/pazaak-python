from functools import reduce
import operator
from typing import List

from dataclasses import dataclass, field

import core.constants as constants
from core.player import Player


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Board:
    board: List[int] = field(
        default_factory=lambda: [
            [constants.EMPTY, constants.EMPTY, constants.EMPTY],
            [constants.EMPTY, constants.EMPTY, constants.EMPTY],
            [constants.EMPTY, constants.EMPTY, constants.EMPTY]
        ])

    def move_new(self, position: Position, player: Player, *args, **kwargs):
        raise NotImplementedError

    def move(self, position: Position, player: Player, *args, **kwargs):
        raise NotImplementedError

    def print(self):
        for row in self.board:
            for col in row:
                print(str(col), end=' ')
            print()

    def full(self, *args, **kwargs):
        return not any(map(lambda x: x == constants.EMPTY, reduce(operator.iconcat, self.board, [])))

    def empty_positions(self, player: Player):
        raise NotImplementedError

    def status(self):
        raise NotImplementedError
