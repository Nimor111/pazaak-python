from dataclasses import dataclass, field

from core.board import Board
from core.player import Player


@dataclass
class State:
    board: Board = field(default_factory=Board)
    win_score: int = field(default=0)
    visit_score: int = field(default=0)
    player: Player = field(default_factory=Player)

    def get_all_states(self, player):
        raise NotImplementedError

    def random_play(self):
        raise NotImplementedError

    def toggle_player(self):
        self.player = self.player.toggle_player()
