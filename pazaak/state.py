from random import choice
from dataclasses import dataclass

from core.state import State
from core.player import Player

from pazaak.player import PazaakPlayer, Card


@dataclass
class PazaakState(State):
    def get_all_states(self, player: PazaakPlayer):
        position = self.board.empty_positions(player)
        all_states = []

        for card in player.cards:
            all_states.append(PazaakState(board=self.board.move_new(position, player, card=card)), player=player)

        # stand
        new_player = Player(player=player.player, stand=True)
        all_states.append(PazaakState(board=self.board, player=new_player))

        # end turn without doing anything
        all_states.append(PazaakState(board=self.board, player=player))

        return all_states

    def random_card(self, player):
        card = Card(score=choice(range(1, 11)))
        position = self.board.empty_positions(player)

        return PazaakState(board=self.board.move_new(position, player, card=card), player=player)
