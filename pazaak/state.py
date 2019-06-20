from dataclasses import dataclass

from core.state import State
from core.player import Player


@dataclass
class PazaakState(State):
    def get_all_states(self, player: Player):
        pass

    def random_play(self):
        pass
