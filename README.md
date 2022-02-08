# Mancala-Game-Using-MiniMax

Using the Minimax algorithm, Mancala game was coded in which the computer and the player can play. There are two difficulty levels in the game, and these levels are determined by the heuristic function used in the minimax function.

MINIMAX ALGORITHM

Minimax algorithm is a decision tree used in artificial intelligence. Basically, in two-player games, it allows the computer to decide and win by taking into account the moves of the other side. Ideal for non-random games.

Approach: Take the move that provides the highest minimax value.

Two different evaluation functions have been written as evaluation functions:

1- Difficult: While determining the score of possible moves, he tries to find the move that will make the number of stones on the other side's board the least and make the most of the stones in his own treasure, and if there is, he tries to put the last stone in an empty treasure so that it will gain the most points.

2- Easy: While determining the score of possible moves, it does not care about the number of pieces on the other side's board, it only tries to find the move that will make the maximum number of stones in its own treasure and the least number of stones in its wells.


SUCCESS OF THE SYSTEM

The game has been played 20 times in two levels.

    DIFFICULTY - TOTAL NUMBER OF GAMES - NUMBER OF GAMES WON - THE SYSTEM ACHIEVEMENT

    Easy                  20                     7                       0.35

    Difficult             20                     17                      0.85

Computer wins:

<img width="317" alt="image" src="https://user-images.githubusercontent.com/44849765/153004363-3cde28ad-7801-4228-a56d-75da47303550.png">

<img width="320" alt="image" src="https://user-images.githubusercontent.com/44849765/153004386-fa63538d-04e6-4a3d-8394-ca9b14bdcb37.png">


Player wins:


<img width="315" alt="image" src="https://user-images.githubusercontent.com/44849765/153004448-647874a2-a313-4f96-8513-a0510a9e54ee.png">

<img width="315" alt="image" src="https://user-images.githubusercontent.com/44849765/153004460-1eb2ae1a-dbfc-4d37-8a71-9b81b9fd9fea.png">
