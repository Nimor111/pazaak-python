import math

from mcts.node import Node


def best_ucb(node: Node):
    best = node
    max_ucb = 0.0

    for child in node.children:
        current_ucb = calculate_ucb_value(
            child.state.win_score,
            child.state.visit_score,
            child.parent.state.visit_score
        )
        if current_ucb >= max_ucb:
            max_ucb = current_ucb
            best = child

    return best


def calculate_ucb_value(win_score: int, visit_score: int, parent_visit_score: int):
    if visit_score == 0:
        return float('inf')

    win_ratio = win_score / visit_score
    exploitation = math.sqrt(math.log(parent_visit_score) / visit_score)

    return win_ratio + 1.41 * exploitation
