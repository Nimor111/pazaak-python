from random import choice

from dataclasses import dataclass, field

from player import Player
from core.board import Board


@dataclass
class State:
    board: Board = field(default_factory=Board)
    win_score: int = field(default=0)
    visit_score: int = field(default=0)
    player: Player = field(default_factory=Player)

    def get_all_states(self, player):
        empty_positions = self.board.empty_positions()
        all_states = []

        for position in empty_positions:
            all_states.append(State(board=self.board.move_new(position, player), player=player))

        return all_states

    def random_play(self):
        pos_to_move = choice(self.board.empty_positions())

        return self.board.move_new(pos_to_move, self.player)

    def toggle_player(self):
        self.player = self.player.toggle_player()
