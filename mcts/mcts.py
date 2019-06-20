from dataclasses import dataclass, field

import core.constants as constants
from core.player import Player

from mcts.node import Node
from mcts.uct import best_uct


@dataclass
class Mcts:
    root: Node = field(default_factory=Node)

    def find_next_move(self, simulations: int):
        self.root.state.toggle_player()
        for _ in range(simulations):
            selected = self.select(self.root)
            if selected.state.board.status() == constants.IN_PROGRESS:
                self.expand_node(selected, selected.state.player)
            node_to_explore = selected
            if len(selected.children) > 0:
                node_to_explore = selected.pick_random_child()

            result = self.simulate(node_to_explore)
            self.backpropagate(node_to_explore, result)

        return self.root.max_visited_child().state.board

    def select(self, node: Node):
        best = self.root

        while len(best.children) != 0:
            best = best_uct(best)

        return best

    def expand_node(self, node: Node, player: Player):
        player = player.toggle_player()
        possible_states = node.state.get_all_states(player)

        for state in possible_states:
            node.children.append(Node(state=state, parent=node))

    def backpropagate(self, node: Node, player: Player):
        temp = node
        while temp is not None:
            temp.state.visit_score += 1
            if temp.state.player == player:
                temp.state.win_score += constants.WIN_SCORE

            temp = temp.parent

    def simulate(self, node: Node):
        curr = node

        board_status = curr.state.board.status()

        while board_status == constants.IN_PROGRESS:
            curr.state.player.toggle_player()
            new_state = curr.state.random_play()
            curr = Node(state=new_state)
            board_status = curr.state.board.status()

        return board_status
