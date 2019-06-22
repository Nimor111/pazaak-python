from tic_tac_toe.board import TicTacBoard
from tic_tac_toe.state import TicTacState
from tic_tac_toe.player import TicTacPlayer

from core.board import Position

from pazaak.board import PazaakBoard
from pazaak.player import Card, PazaakPlayer

from mcts.node import Node
from mcts.mcts import Mcts


def pazaak():
    b = PazaakBoard()

    b = b.move_new(Position(0, 0), PazaakPlayer(player=2), card=Card(5))
    print(b.status())
    b.print()


def tic_tac_toe():
    b = TicTacBoard()

    state = TicTacState(board=b, player=TicTacPlayer(1))

    while b.status() == -1:
        node = Node(state=state)
        tree = Mcts(root=node)

        print(">>>>> CURR PLAYER: <<<<<<<", state.player.player)
        b = tree.find_next_move(7000)
        state = TicTacState(board=b, player=state.player)
        print("TURN\n")
        b.print()


def main():
    pazaak()


if __name__ == "__main__":
    main()
