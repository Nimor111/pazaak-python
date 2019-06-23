from copy import deepcopy

from dataclasses import dataclass

from tic_tac_toe.player import TicTacPlayer
import core.constants as constants

from core.board import Board, Position


@dataclass
class TicTacBoard(Board):
    def move_new(self, position: Position, player: TicTacPlayer):
        new_board = deepcopy(self.board)
        new_board[position.x][position.y] = player.player

        return TicTacBoard(board=new_board)

    def move(self, position: Position, player: TicTacPlayer):
        self.board[position.x][position.y] = player.player

    def empty_positions(self):
        positions = []

        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == constants.EMPTY:
                    positions.append(Position(row, col))

        return positions

    def status(self):
        # rows
        for i in range(constants.BOARD_SIZE):
            if self.board[i][0] != constants.EMPTY and self.board[i][1] != constants.EMPTY\
                and self.board[i][2] != constants.EMPTY and self.board[i][0] == self.board[i][1]\
                    and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]

        # cols
        transposed = Board()

        for i in range(constants.BOARD_SIZE):
            for j in range(constants.BOARD_SIZE):
                transposed.board[i][j] = self.board[j][i]

        for i in range(constants.BOARD_SIZE):
            if transposed.board[i][0] != constants.EMPTY and transposed.board[i][1] != constants.EMPTY\
                and transposed.board[i][2] != constants.EMPTY and transposed.board[i][0] == transposed.board[i][1]\
                    and transposed.board[i][1] == transposed.board[i][2]:
                return transposed.board[i][0]

        # prim diag
        if self.board[0][0] != constants.EMPTY and self.board[1][1] != constants.EMPTY\
            and self.board[2][2] != constants.EMPTY and self.board[0][0] == self.board[1][1]\
                and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]

        # secondary diag
        if self.board[0][2] != constants.EMPTY and self.board[1][1] != constants.EMPTY\
            and self.board[2][0] != constants.EMPTY and self.board[0][2] == self.board[1][1]\
                and self.board[2][0] == self.board[1][1]:
            return self.board[0][2]

        # draw
        if self.full():
            return constants.DRAW

        # in progress
        return constants.IN_PROGRESS
