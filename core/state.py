from typing import List
from random import choice
from dataclasses import dataclass, field

from core.board import Board
from core.player import Player


@dataclass
class State:
    board: Board = field(default_factory=Board)
    win_score: int = field(default=0)
    visit_score: int = field(default=0)
    players: List[Player] = field(default_factory=list)
    player: Player = field(default_factory=Player)
    player_index: int = field(default=0)

    def get_all_states(self, player):
        raise NotImplementedError

    def random_play(self):
        return choice(self.get_all_states(self.player))

    def toggle_player(self):
        self.player_index = 1 - self.player_index
        self.player = self.players[self.player_index]

        return self.player

    def toggle_player_new(self):
        return self.players[1 - self.player_index]
