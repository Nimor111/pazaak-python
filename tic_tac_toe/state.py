from random import choice

from dataclasses import dataclass

from core.state import State


@dataclass
class TicTacState(State):
    def get_all_states(self, player):
        empty_positions = self.board.empty_positions()
        all_states = []

        for position in empty_positions:
            all_states.append(TicTacState(board=self.board.move_new(position, player), player=player))

        return all_states

    def random_play(self):
        pos_to_move = choice(self.board.empty_positions())

        return TicTacState(board=self.board.move_new(pos_to_move, self.player), player=self.player)

    def toggle_player(self):
        self.player = self.player.toggle_player()
