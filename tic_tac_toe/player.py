from dataclasses import dataclass

from core.player import Player


@dataclass
class TicTacPlayer(Player):
    def toggle_player(self):
        return TicTacPlayer(player=3 - self.player)

    def toggle_player_new(self, player: 'TicTacPlayer'):
        return TicTacPlayer(player=player)
