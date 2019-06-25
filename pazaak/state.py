from random import choice
from dataclasses import dataclass

from core.state import State

from pazaak.player import PazaakPlayer, Card


@dataclass
class PazaakState(State):
    def get_all_states(self, player: PazaakPlayer):
        position = self.board.empty_positions(player)
        all_states = []

        for card in player.side_deck:
            all_states.append(
                PazaakState(
                    board=self.board.move_new(position, player, card=card),
                    player=player,
                    players=self.players,
                    player_index=player.player - 1
                )
            )

        # stand
        new_player = PazaakPlayer(player=player.player, stand=True, side_deck=player.side_deck)
        all_states.append(
            PazaakState(
                board=self.board,
                player=new_player,
                players=self.players,
                player_index=player.player - 1
            )
        )

        # end turn without doing anything
        all_states.append(
            PazaakState(
                board=self.board,
                player=player,
                players=self.players,
                player_index=player.player - 1
            )
        )

        return all_states

    def random_card(self):
        card = Card(score=choice(range(1, 11)))
        position = self.board.empty_positions(self.player)

        return PazaakState(
            board=self.board.move_new(position, self.player, card=card),
            players=self.players,
            player=self.player,
            player_index=self.player_index
        )

    def random_play(self):
        self.state = self.random_card()
        return choice(self.get_all_states(self.player))
