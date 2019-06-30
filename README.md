# AI for Pazaak with MCTS ( Monte Carlo Tree Search )

Repository: [Pazaak](https://github.com/Nimor111/pazaak-python)

## About the game

Official page: [Pazaak](https://starwars.fandom.com/wiki/Pazaak/Legends)

### TL;DR

* Similar to Blackjack, players place bets
* Two players who each have a 3x3 board, taking turns, starting at 0 result
* Every turn a random card is drawn by each of the players and is added to his board and his current result
* Every player draws four cards in the beginning of the game that act as a side deck. These cards can add to and subtract to current score, can also multiply it etc.
* Every turn, a player can:
  * Use *one* card from the side deck to modify their current result
  * To *stand down*, which suspends his turns for the current game
  * To *end* his turn, which finishes his turn with the current result

The game ends when any player has won two out of three sets. Each set is won in three scenarios:
* A player has 20 points
* A player has > 20 points - the other player wins
* A player's board is full - the player with the most score wins

### How the game looks originally
![pazaak.png](https://vignette.wikia.nocookie.net/starwars/images/6/60/Pazaak%28KOTOR2%29.jpg/revision/latest?cb=20060504165658)

## AI

Cards are drawn at random from the deck which implies a probabilistic nature to the game. Since the branching factor of a minimax solution would be very big and the time for computing the optimal solution would be too big. We can consider a Monte Carlo approach - random sampling of game states and building a Monte Carlo Search Tree and performing simulations until an optimal solution is found. For each node of the tree, we keep a win count based on how many simulations through this node have reached a win condition for the current player and also a visit count for how many times we've passed through this node. Each node is a (valid) game state.

There are four phases to the MCTS algorithm:

* Selection: Starting with a root node, the algorithm selects a child node with the maximum win rate. (We need to find a good way to select optimal child nodes until we reach a leaf in the tree (e.g. a win state))
* Expansion: If we can't select an optimal node anymore, we expand the tree by attaching all possible next states from the leaf node.
* Simulation: After expansion, a child node is picked at random and a random succession of moves is done until a final state is reached.
* Backpropagation: When the end of the game is reached, the nodes that have been visited in the simulation are updated with a win score and a visit score. (If the current player has won the simulation the nodes' win and visitscore is updated, otherwise only the visit score is.)

**This is done for a fixed number of iterations or a fixed duration. In the end, we take the child with the max score of the root and that is the optimal move for the AI to take.**
