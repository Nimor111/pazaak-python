from dataclasses import dataclass

from core.board import Board, Position

from pazaak.player import PazaakPlayer


@dataclass
class PazaakBoard(Board):
    def move_new(self, position: Position, player: PazaakPlayer):
        pass

    def move(self, position: Position, player: PazaakPlayer):
        pass

    def empty_positions(self):
        pass

    def status(self):
        pass
