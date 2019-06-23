from typing import List
from dataclasses import dataclass, field

from core.player import Player


@dataclass
class Card:
    score: int = field(default=0)


@dataclass
class PazaakPlayer(Player):
    stand: bool = field(default=False)
    side_deck: List[Card] = field(default=list)

    def toggle_player(self):
        if not self.stand:
            return PazaakPlayer(player=3-self.player)

        return self

    def toggle_player_new(self, player: 'PazaakPlayer'):
        if not self.stand:
            return PazaakPlayer(player=player)

        return self
