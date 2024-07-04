from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax, X, O, EMPTY
import pytest


def test_initial_state():
    board = initial_state()
    expected_board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    assert board == expected_board


def test_player():
    board = [
        [X, O, X],
        [O, X, None],
        [None, None, None]
    ]
    assert player(board) == O

    board = [
        [X, O, X],
        [O, X, None],
        [None, O, None]
    ]
    assert player(board) == X


def test_actions():
    board = [
        [X, O, X],
        [O, X, None],
        [None, None, None]
    ]
    expected_actions = {(1, 2), (2, 0), (2, 1), (2, 2)}
    assert actions(board) == expected_actions


def test_result():
    board = initial_state()
    action = (1, 1)
    new_board = result(board, action)
    expected_board = [
        [None, None, None],
        [None, X, None],
        [None, None, None]
    ]
    assert new_board == expected_board

    try:
        result(new_board, action)  # Trying to move on an occupied cell
    except Exception as e:
        assert str(e) == "Invalid action"


def test_winner():
    board = [
        [X, X, X],
        [O, O, None],
        [None, None, None]
    ]
    assert winner(board) == X

    board = [
        [X, O, X],
        [X, O, None],
        [None, O, None]
    ]
    assert winner(board) == O

    board = [
        [X, O, X],
        [X, O, None],
        [None, None, None]
    ]
    assert winner(board) is None


def test_terminal():
    board = [
        [X, X, X],
        [O, O, None],
        [None, None, None]
    ]
    assert terminal(board)

    board = [
        [X, O, X],
        [X, O, None],
        [None, None, None]
    ]
    assert not terminal(board)


def test_utility():
    board = [
        [X, X, X],
        [O, O, None],
        [None, None, None]
    ]
    assert utility(board) == 1

    board = [
        [X, O, X],
        [X, O, None],
        [None, O, None]
    ]
    assert utility(board) == -1

    board = [
        [X, O, X],
        [X, O, None],
        [None, None, None]
    ]
    assert utility(board) == 0


def test_minimax():
    board = [
        [X, O, X],
        [O, X, None],
        [None, None, O]
    ]
    optimal_moves = {(1, 2), (2, 0)}
    assert minimax(board) in optimal_moves
