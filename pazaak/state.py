from random import choice
from dataclasses import dataclass

import core.constants as constants
from core.state import State

from pazaak.player import PazaakPlayer, Card


@dataclass
class PazaakState(State):
    def get_all_states(self, player: PazaakPlayer):
        position = self.board.empty_positions(player)
        all_states = []

        for card in player.side_deck:
            new_state = PazaakState(
                board=self.board.move_new(position, player, card=card),
                player=player,
                players=self.players,
                player_index=player.player - 1
            )
            board_size = len(new_state.board.board)

            player_score = self.board._calculate_score(0, board_size // 2)
            opponent_score = self.board._calculate_score(board_size // 2, board_size)

            if player.player == constants.PLAYER and player_score == constants.END_SCORE:
                new_state.player = PazaakPlayer(player=player.player, stand=True, side_deck=player.side_deck)
                new_state.players = [new_state.player, self.players[1]]

            if player.player == constants.OPPONENT and opponent_score == constants.END_SCORE:
                new_state.player = PazaakPlayer(player=player.player, stand=True, side_deck=player.side_deck)
                new_state.players = [self.players[0], new_state.player]

            all_states.append(new_state)

        # stand
        new_players = []
        new_player = PazaakPlayer(player=player.player, stand=True, side_deck=player.side_deck)
        if self.player_index == 0:
            new_players = [self.players[0], new_player]
        else:
            new_players = [new_player, self.players[1]]

        all_states.append(
            PazaakState(
                board=self.board,
                player=new_player,
                players=new_players,
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
        if self.player.stand:
            self.player_index = self.player.player - 1
            return self

        self = self.random_card()
        return choice(self.get_all_states(self.player))
