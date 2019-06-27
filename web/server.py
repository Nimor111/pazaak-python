import os
from flask import Flask, jsonify
from random import choice

from pazaak.board import PazaakBoard
from pazaak.state import PazaakState
from pazaak.player import Card, PazaakPlayer

from mcts.node import Node
from mcts.mcts import Mcts

app = Flask(__name__)
port = int(os.getenv('PORT', 3000))


def init_game():
    board = PazaakBoard()
    player_side_deck = [Card(x) for x in [choice(range(1, 7)) for _ in range(4)]]
    opponent_side_deck = [Card(x) for x in [choice(range(1, 7)) for _ in range(4)]]

    players = [
        PazaakPlayer(player=1, side_deck=player_side_deck),
        PazaakPlayer(player=2, side_deck=opponent_side_deck)
    ]

    state = PazaakState(board=board, players=players, player=players[0])

    return state


app_state = init_game()


def get_next_board():
    global app_state
    if app_state.board.status(players=app_state.players) == -1:
        if not app_state.player.stand:
            app_state = app_state.random_card()

        node = Node(state=app_state)
        tree = Mcts(root=node)

        app_state.board = tree.find_next_move(100)
        app_state = PazaakState(
            board=app_state.board,
            player=app_state.player,
            players=app_state.players,
            player_index=app_state.player_index
        )

        return app_state.board

    return app_state.board


@app.route('/reset')
def reset():
    global app_state
    app_state = init_game()
    return jsonify(board=app_state.board.board)


@app.route('/current-state')
def init():
    return jsonify(board=app_state.board.board)


@app.route('/next-state')
def next_state():
    next_board = get_next_board()

    return jsonify(board=next_board.board)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
