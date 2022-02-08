from typing import List, Any

import numpy as np
import time

MIN = 1
MAX = 0
difficulty = 1


def main():
    # which player will start
    player = np.random.randint(2)

    run_the_game(player)


def run_the_game(player):
    board = np.array([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0])
    end = False
    onlyone = False
    doesntmatter = False

    difficulty = input("Kolay icin 0, Zor icin 1 secin")
    print(">> GAME BEGINS <<")
    print("")
    print_board(board)

    while not end:
        # eger rakibin kuyusuna tas koymaya baslarsan move2 ile hareket edecek, baslangic olarak move2 yi 0 la
        print("")

        # bilgisayar hamlesini secsin
        if player == 0:
            print("Computers turn...")
            time.sleep(1.3)
            # if there is one only one move to take, dont use minimax algorithm
            onlyone = check_for_one(board)
            if onlyone:
                one = find_one_move(board)
                move = one
            else:
                # use minimax algorithm to find the move
                move = comp_choose_move(board)
            print("Computer moved at", move)
            doesntmatter = take_move(board, move, MAX)
            print_board(board)
            print("________________________________________________________")
            end = check_board(board)
            if end:
                break
            else:
                player = 1  # switch turn so that the human can go.

        # kullanici hamlesini secsin
        else:
            print("Your turn...")
            print_board(board)
            choiceofmove = ask_for_selection(board)
            print("")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - >  >  >  >  > ")
            print("")
            doesntmatter = take_move(board, choiceofmove, MIN)
            print_board(board)
            print ("________________________________________________________")
            end = check_board(board)
            if end:
                break
            else:
                player = 0

    print(">>> GAME OVER <<<")
    if board[6] > board[13]:
        print("You Win with a score ", board[6])
    elif board[13] > board[6]:
        print("Computer Wins with a score ", board[13])
    else:
        print("Game is a tie!")
    print_board(board)


def ask_for_selection(board):
    print("Choose your move")
    select = input("You can choose either 0, 1, 2, 3, 4 or 5")
    select = int(select)
    while select > 5 or select < 0 or board[select] == 0:  # make sure valid selection
        print("Wrong selection")
        print("Choose your move")
        select = input("You can choose either 0, 1, 2, 3, 4 or 5")
        select = int(select)
    return select


def comp_choose_move(board):
    depth = 2
    alpha = -999
    beta = 999
    maxD = 2
    moveScore, moveBinNum = minimax(board, 0, maxD, 0, alpha, beta)
    return moveBinNum


def minimax(board, d, maxD, minOrMax, alpha, beta):
    check = check_board(board)
    # check if the game is over, if its over dont resume the game
    if check:
        if minOrMax == MIN:  # computer is playing
            score = -999
            binNum = -1
            return score, binNum
        elif minOrMax == MAX:
            score = 999
            binNum = -1
            return score, binNum
    elif d == maxD:
        if difficulty == 1:
            score = get_heurestic_score(board, minOrMax)
        if difficulty == 0:
            score = get_heurestic_score_dum(board, minOrMax)
        binNum = -1
        return score, binNum
    else:
        if minOrMax == MIN:  # minimizing player
            score = 999
            binNum = -1
            for i in range(0, 6):
                if board[i] != 0:
                    # Copy board into board2
                    board2 = np.copy(board)
                    doesntmatter = take_move(board, i, minOrMax)
                    # recursive call minmax with m.score(as beta) and alpha
                    mTempScore, mTempBinNum = minimax(board, d + 1, maxD, MAX, alpha, score)
                    if score <= alpha:
                        break
                    if mTempScore < score:
                        score = mTempScore
                        binNum = i
                    for k in range (0, 14):
                        board[k] = board2[k]

            return score, binNum
        elif minOrMax == MAX:
            score = -999
            binNum = -1
            for i in range(7, 13):
                if board[i] != 0:
                    # Copy board into board2
                    board2 = np.copy(board)
                    doesntmatter = take_move(board, i, minOrMax)
                    # recursive call minmax with m.score(as alpha) and beta
                    mTempScore, mTempBinNum = minimax(board, d + 1, maxD, MIN, score,beta)
                    if score > beta:
                        break
                    if mTempScore >= score:
                        score = mTempScore
                        binNum = i
                    for k in range(0, 14):
                        board[k] = board2[k]

            return score, binNum


def take_move(board, choice, minOrMax):
    if minOrMax == MAX:  # computer playing
        avoid = 6   # dont put stones to opponent players treasure (6)
    else:  # human playing
        avoid = 13  # dont put stones to opponent players treasure (13)
    picked = board[choice]
    next = choice + 1
    if next == avoid:
        if avoid == 13:
            next = 0
        elif avoid == 6:
            next = 7
    board[choice] = 0

    changed = False
    while picked > 0:
        if next == avoid:
            if avoid == 13:
                changed = True
                next = 0  # since we are avoiding 13, the next bin is 0
            else:
                changed = True
                next = 7  # since we are avoiding 6, the next bin is 7

        currentinnext = board[next]
        board[next] = currentinnext + 1  # add one to the value of the marbles in the next bin
        test = picked - 1

        if test >= 0:
            if changed:
                next += 1
                if next == 14:
                    next = 0
            elif picked == 1 and currentinnext == 0:
                board[next] = 1
                break
            else:
                next += 1
                if next == 14:
                    next = 0
        picked = picked - 1

    ending = next - 1
    if ending == -1:
        ending = 13
    elif ending == 7:
        ending = 6

    if MAX == minOrMax and ending == 6:
        ending = ending + 1

    if MAX == minOrMax:  # this is a special condition that had to be hardcoded
      ending = ending + 1

    if MIN == minOrMax:
       ending = ending + 1

    # make sure that it doesn't find across if landed in mancala
    if ending != 13 and ending != 6:
        if MIN == minOrMax and -1 < ending < 6 and board[ending] == 1:  # for human
            # to take the opponent players across bins stones, learn the position of the across bin
            across = findacross(ending)
            if board[across] > 0:
                x = board[across]
                board[6] = board[6] + 1 + x
                board[ending] = 0
                board[across] = 0
                return True
            else:
                return False
        if MAX == minOrMax and 6 < ending < 13 and board[ending] == 1:
            # to take the opponent players across bins stones, learn the position of the across bin
            across = findacross(ending)
            if board[across] > 0:
                x = board[across]
                board[13] = board[13] + 1 + x
                board[ending] = 0
                board[across] = 0
                return True
            else:
                return False
    else:
        return False

    return False


def check_board(board):
    humannumempty = 0
    # check the human players side
    for i in range(0, 6):
        if board[i] == 0:
            humannumempty += 1
    # if human ends the game first, human takes computers stones
    if humannumempty == 6:
        board[6] = board[6] + board[12] + board[11] + board[10] + board[9] + board[8] + board[7]
        for i in range(7, 13):
            board[i] = 0  # empty all on computer side
        return True

    # check the computer players side
    compnumempty = 0
    for i in range(7, 13):
        if board[i] == 0:
            compnumempty += 1
    # if cumputer ends the game first, computer takes humans stones
    if compnumempty == 6:
        board[13] = board[13] + board[5] + board[4] + board[3] + board[2] + board[1] + board[0]
        for i in range(0, 6):
            board[i] = 0  # empty all on human side
        return True

    return False  # if not empty return False


def find_one_move(board):
    check = 0
    for i in range(7, 13):
        if board[i] > 0:
            check = i
            return check


def check_for_one(board):
    check = 0
    for i in range(7, 13):
        if board[i] > 0:
            check = check + 1
    if check == 1:
        return True
    else:
        return False


def get_heurestic_score(board, minOrMax):
    score = 0
    board2 = np.copy(board)
    humanside = (board[0] + board[1] + board[2] + board[3] + board[4] + board[5]) * 0.45
    humanmancala = (board[6]) * 3.45
    human = humanside + humanmancala

    compside = (board[7] + board[8] + board[9] + board[10] + board[11] + board[12]) * 0.45
    compmancala = (board[13]) * 3.45
    comp = compside + compmancala
    difference_board = comp - human
    valueofboard = int(difference_board + 0.5)
    for i in range(0, 6):
        checkempty = take_move(board2, i, minOrMax)
        if checkempty:  # if you can land in an empty bin
            acrosslocation = findacross(i)
            acrosspieces = board2[acrosslocation]
            valueofboard = valueofboard + ((acrosspieces * 0.5) * -1)
    for i in range(7, 13):
        checkempty = take_move(board2, i, minOrMax)
        if checkempty:  # if you can land in an empty bin
            acrosslocation = findacross(i)
            acrosspieces = board2[acrosslocation]
            valueofboard = valueofboard + (acrosspieces * 0.5)

    valueofboard = int(valueofboard)
    return valueofboard


def get_heurestic_score_dum(board, minOrMax):
    score = 0
    board2 = np.copy(board)

    compside = (board[7] + board[8] + board[9] + board[10] + board[11] + board[12]) * 0.45
    compmancala = (board[13]) * 3.45
    comp = compside + compmancala

    valueofboard = int(comp + 0.5)
    return valueofboard


def findacross(ending):
    across = -10
    if ending == 0:
        across = 12
    elif ending == 1:
        across = 11
    elif ending == 2:
        across = 10
    elif ending == 3:
        across = 9
    elif ending == 4:
        across = 8
    elif ending == 5:
        across = 7
    elif ending == 6:
        across = 6
    elif ending == 7:
        across = 5
    elif ending == 8:
        across = 4
    elif ending == 9:
        across = 3
    elif ending == 10:
        across = 2
    elif ending == 11:
        across = 1
    elif ending == 12:
        across = 0
    return across


def print_board(board):
    print("                  12  11  10  9   8   7      ")
    print("                  -   -   -   -   -   - ")
    print("            |   |", board[12], " ", board[11], " ", board[10], " ", board[9], " ", board[8], " ", board[7],
          "|   |")
    print("Computer -> |", board[13], "|                       |", board[6], "|  <- Player")
    print("            |   |", board[0], " ", board[1], " ", board[2], " ", board[3], " ", board[4], " ", board[5],
          "|   |")
    print("              -   -   -   -   -   -   - ")
    print("                  0   1   2   3   4   5 ")


if __name__ == "__main__":
    main()
