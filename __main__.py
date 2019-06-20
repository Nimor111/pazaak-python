from tic_tac_toe.board import TicTacBoard
from tic_tac_toe.state import TicTacState
from tic_tac_toe.player import TicTacPlayer

from mcts.node import Node
from mcts.mcts import Mcts


def main():
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


if __name__ == "__main__":
    main()
