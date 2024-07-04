"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    The player with fewer moves on the board goes next.
    If both players have made the same number of moves, X goes next.
    """
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)
    return X if count_X == count_O else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    An action is represented as a tuple of two integers, indicating the row and column of the move.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    The move is made by the current player on a copy of the board.
    Raises an exception if the action is invalid (i.e., not on an empty cell).
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    new_board = [row.copy() for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Checks all rows, columns, and diagonals for a winning line of three Xs or Os.
    Returns 'X' if X wins, 'O' if O wins, and None otherwise.
    """
    lines = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for line in lines:
        symbols = [board[i][j] for i, j in line]
        if symbols.count(X) == 3:
            return X
        elif symbols.count(O) == 3:
            return O

    return None


def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    The game is over if there is a winner or if there are no empty cells left.
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    This function assumes that the game is over.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Uses the minimax algorithm to determine the best move.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_score = float('-inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            score = min_value(new_board)
            if score > best_score:
                best_score = score
                best_action = action
    else:
        best_score = float('inf')
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            score = max_value(new_board)
            if score < best_score:
                best_score = score
                best_action = action

    return best_action


def max_value(board):
    """
    Helper function for the minimax algorithm.
    Returns the maximum utility value for the current board.
    """
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Helper function for the minimax algorithm.
    Returns the minimum utility value for the current board.
    """
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
