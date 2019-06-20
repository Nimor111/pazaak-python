import math

from mcts.node import Node


def best_uct(node: Node):
    best = node
    max_uct = 0.0

    for child in node.children:
        current_uct = calculate_uct_value(
            child.state.win_score,
            child.state.visit_score,
            child.parent.state.visit_score
        )
        if current_uct >= max_uct:
            max_uct = current_uct
            best = child

    return best


def calculate_uct_value(win_score: int, visit_score: int, parent_visit_score: int):
    if visit_score == 0:
        return float('inf')

    win_ratio = win_score / visit_score
    exploitation = math.sqrt(math.log(parent_visit_score) / visit_score)

    return win_ratio + 1.41 * exploitation
