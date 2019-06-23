from dataclasses import dataclass

from core.state import State

from tic_tac_toe.player import TicTacPlayer


@dataclass
class TicTacState(State):
    def get_all_states(self, player: TicTacPlayer):
        empty_positions = self.board.empty_positions()
        all_states = []

        for position in empty_positions:
            all_states.append(
                TicTacState(
                    board=self.board.move_new(position, player),
                    player=player,
                    players=self.players,
                    player_index=player.player - 1
                )
            )

        return all_states

    def toggle_player_new(self):
        return self.players[1 - self.player_index]
