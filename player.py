from dataclasses import dataclass, field


@dataclass
class Player:
    player: int = field(default=0)

    def toggle_player(self):
        return Player(player=3 - self.player)


# class TicTacPlayer(Player):
#     def toggle_player(self):
#         self.player = 3 - self.player
