from dataclasses import dataclass, field

from core.player import Player


@dataclass
class Card:
    score: int = field(default=0)


@dataclass
class PazaakPlayer(Player):
    def toggle_player(self):
        return PazaakPlayer(player=3 - self.player)
