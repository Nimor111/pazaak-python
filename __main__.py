import random
from datetime import datetime

from board import Board
from state import State
from player import Player
from node import Node
from mcts import Mcts


def main():
    b = Board()

    state = State(board=b, player=Player(1))

    while b.status() == -1:
        node = Node(state=state)
        tree = Mcts(root=node)

        # __import__('ipdb').set_trace()
        print(">>>>> CURR PLAYER: <<<<<<<", state.player.player)
        b = tree.find_next_move(7000)
        # __import__('ipdb').set_trace()
        state = State(board=b, player=state.player)
        print("TURN\n")
        b.print()


if __name__ == "__main__":
    main()
