from dataclasses import dataclass, field


@dataclass
class Player:
    player: int = field(default=0)

    def toggle_player(self):
        raise NotImplementedError

    def toggle_player_new(self, player: 'Player'):
        raise NotImplementedError
