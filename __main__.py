from random import choice

from tic_tac_toe.board import TicTacBoard
from tic_tac_toe.state import TicTacState
from tic_tac_toe.player import TicTacPlayer

from pazaak.board import PazaakBoard
from pazaak.player import Card, PazaakPlayer
from pazaak.state import PazaakState

from mcts.node import Node
from mcts.mcts import Mcts


def pazaak():
    b = PazaakBoard()
    player_side_deck = [Card(x) for x in [choice(range(1, 7)) for _ in range(4)]]
    opponent_side_deck = [Card(x) for x in [choice(range(1, 7)) for _ in range(4)]]

    players = [
        PazaakPlayer(player=1, side_deck=player_side_deck),
        PazaakPlayer(player=2, side_deck=opponent_side_deck)
    ]

    state = PazaakState(
        board=b,
        players=players,
        player=players[0]
    )

    while b.status() == -1:
        state = state.random_card()
        node = Node(state=state)
        tree = Mcts(root=node)

        print(">>>>> CURR PLAYER: <<<<<<<", state.player.player)
        b = tree.find_next_move(100)
        state = PazaakState(board=b, player=state.player, players=state.players, player_index=state.player_index)
        print("TURN\n")
        b.print()


def tic_tac_toe():
    b = TicTacBoard()

    players = [TicTacPlayer(1), TicTacPlayer(2)]
    state = TicTacState(board=b, player=players[0], players=players)

    while b.status() == -1:
        node = Node(state=state)
        tree = Mcts(root=node)

        print(">>>>> CURR PLAYER: <<<<<<<", state.player.player)
        b = tree.find_next_move(100)
        state = TicTacState(board=b, player=state.player, players=state.players, player_index=state.player_index)
        print("TURN\n")
        b.print()


def main():
    pazaak()


if __name__ == "__main__":
    main()
