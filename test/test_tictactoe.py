# test_tictactoe.py

import pytest
from tictactoe import initialize_board, make_move, check_winner, reset_game

def test_initialize_board():
    """Test that initialize_board creates a 3x3 board of empty spaces."""
    board = initialize_board()
    assert board == [[' ' for _ in range(3)] for _ in range(3)]

def test_make_move_valid():
    """Test that a valid move is made and the board is updated."""
    board = initialize_board()
    assert make_move(board, 1, 1, 'X') == True
    assert board[1][1] == 'X'

def test_make_move_invalid():
    """Test that an invalid move (on an occupied cell) returns False."""
    board = initialize_board()
    make_move(board, 1, 1, 'X')  # First move is valid
    assert make_move(board, 1, 1, 'O') == False  # Cannot overwrite

def test_check_winner():
    """Test that check_winner correctly identifies the winner."""
    board = [['X', 'X', 'X'],
             [' ', 'O', ' '],
             [' ', 'O', ' ']]
    assert check_winner(board) == 'X'

def test_check_draw():
    """Test that check_winner identifies a draw."""
    board = [['X', 'O', 'X'],
             ['X', 'O', 'O'],
             ['O', 'X', 'X']]
    assert check_winner(board) == 'Draw'

def test_reset_game():
    """Test that reset_game reinitializes the board."""
    board = [['X', 'X', 'X'],
             [' ', 'O', ' '],
             [' ', 'O', ' ']]
    new_board = reset_game()
    assert new_board == [[' ' for _ in range(3)] for _ in range(3)]

def test_game_integration():
    """Test integration of game functions by simulating a game."""
    board = initialize_board()
    assert make_move(board, 0, 0, 'X') == True
    assert make_move(board, 1, 1, 'O') == True
    assert make_move(board, 0, 1, 'X') == True
    assert make_move(board, 2, 2, 'O') == True
    assert make_move(board, 0, 2, 'X') == True
    assert check_winner(board) == 'X'
    new_board = reset_game()
    assert new_board == [[' ' for _ in range(3)] for _ in range(3)]

# Advanced Tests

@pytest.mark.parametrize("initial_board, row, col, player, expected", [
    ([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 0, 'X', True),
    ([['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], 0, 0, 'O', False),
    ([[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']], 1, 1, 'O', False),
    ([['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']], 3, 3, 'X', IndexError),
    ([['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']], -1, 0, 'O', IndexError),
])
def test_make_move_parametrize(initial_board, row, col, player, expected):
    """Parameterized test to check different move scenarios."""
    board = initial_board
    if expected == IndexError:
        with pytest.raises(IndexError):
            make_move(board, row, col, player)
    else:
        assert make_move(board, row, col, player) == expected

# Fixtures for setting up a fresh board
@pytest.fixture
def fresh_board():
    """Fixture for setting up a fresh board before each test."""
    return initialize_board()

def test_fixture_board(fresh_board):
    """Test that fixture creates a fresh empty board."""
    assert fresh_board == [[' ' for _ in range(3)] for _ in range(3)]
