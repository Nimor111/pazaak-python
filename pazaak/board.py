from functools import reduce
import operator
from typing import List
from copy import deepcopy
from dataclasses import dataclass, field

from core.board import Board, Position
import core.constants as constants

from pazaak.player import PazaakPlayer


@dataclass
class PazaakBoard(Board):
    board: List[int] = field(
        default_factory=lambda: [
            # first player half
            [constants.EMPTY, constants.EMPTY, constants.EMPTY],
            [constants.EMPTY, constants.EMPTY, constants.EMPTY],
            [constants.EMPTY, constants.EMPTY, constants.EMPTY],
            # second player half
            [constants.EMPTY, constants.EMPTY, constants.EMPTY],
            [constants.EMPTY, constants.EMPTY, constants.EMPTY],
            [constants.EMPTY, constants.EMPTY, constants.EMPTY],
        ])

    def move_new(self, position: Position, player: PazaakPlayer, *args, **kwargs):
        if player.stand:
            return PazaakBoard(board=self.board)

        new_board = deepcopy(self.board)
        card = kwargs.get('card')
        new_board[position.x][position.y] = card.score

        return PazaakBoard(board=new_board)

    def move(self, position: Position, player: PazaakPlayer, *args, **kwargs):
        if player.stand:
            return PazaakBoard(board=self.board)

        card = kwargs.get('card')
        self.board[position.x][position.y] = card.score

    def empty_positions(self, player: PazaakPlayer):
        if player.player == constants.PLAYER:
            return self._empty_positions_by_player(0, len(self.board) // 2)
        elif player.player == constants.OPPONENT:
            return self._empty_positions_by_player(len(self.board) // 2, len(self.board))

    def _empty_positions_by_player(self, start: int, end: int):
        for row in range(start, end):
            for col in range(len(self.board) // 2):
                if self.board[row][col] == constants.EMPTY:
                    return Position(row, col)

    def print(self):
        board_string = ''

        board_string = self._print(board_string, 0, len(self.board) // 2)

        board_string += ('_ ' * (len(self.board) // 2)).strip()
        board_string += '\n\n'

        board_string = self._print(board_string, len(self.board) // 2, len(self.board))

        print(board_string)

    def _print(self, board_string: str, start: int, end: int):
        for row in range(start, end):
            for col in range(len(self.board) // 2):
                board_string = board_string + str(self.board[row][col]) + ' '
            board_string = board_string + '\n'

        return board_string

    def full(self, *args, **kwargs):
        player = kwargs.get('player')

        if player == constants.PLAYER:
            return self._full(0, len(self.board) // 2)
        elif player == constants.OPPONENT:
            return self._full(len(self.board) // 2, len(self.board))

    def _full(self, start: int, end: int):
        return not any(map(lambda x: x == constants.EMPTY, reduce(operator.iconcat, self.board[start:end], [])))

    # TODO handle case when someone has a stand
    def status(self):
        board_size = len(self.board)

        player_score = sum(reduce(operator.iconcat, self.board[:board_size // 2], []))
        opponent_score = sum(reduce(operator.iconcat, self.board[board_size // 2:board_size], []))

        if player_score == constants.END_SCORE and opponent_score == constants.END_SCORE:
            return constants.DRAW

        if player_score > constants.END_SCORE:
            return constants.OPPONENT

        if opponent_score > constants.END_SCORE:
            return constants.PLAYER

        if self.full(player=constants.PLAYER):
            return constants.PLAYER

        if self.full(player=constants.OPPONENT):
            return constants.OPPONENT

        return constants.IN_PROGRESS
