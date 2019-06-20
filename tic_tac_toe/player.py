from dataclasses import dataclass

from core.player import Player


@dataclass
class TicTacPlayer(Player):
    def toggle_player(self):
        return TicTacPlayer(player=3 - self.player)
