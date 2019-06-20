from random import choice
from typing import List
from operator import attrgetter

from dataclasses import dataclass, field

from core.state import State


@dataclass
class Node:
    state: State = field(default_factory=State)
    parent: 'Node' = field(default=None)
    children: List['Node'] = field(default_factory=list)

    def pick_random_child(self):
        return choice(self.children)

    def max_visited_child(self):
        return max(self.children, key=attrgetter('state.visit_score'))
