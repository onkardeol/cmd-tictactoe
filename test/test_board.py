import unittest
from unittest.mock import Mock, patch, PropertyMock
from src.board import Board
from src.player import Player

class TestBoard(unittest.TestCase):
    BOARD_SIZE = 3

    def setUp(self):
        self.sut = Board()
        self.player_x = Player('X')
        self.player_o = Player('O')

    def test_play_move_returns_true_with_valid_moves(self):
        for i in range(1, self.BOARD_SIZE ** 2 + 1):
            self.assertTrue(self.sut.play_move(i, self.player_x))

    def test_play_move_raises_exception_if_pos_is_occupied(self):
        self.sut.board[0][0] = self.player_x.name
        self.assertRaises(ValueError, self.sut.play_move, 1, self.player_o)

    def test_validate_move_returns_true_when_move_is_valid(self):
        for i in range(1, self.BOARD_SIZE ** 2 + 1):
            self.assertTrue(self.sut.validate_move(i))
    
    def test_validate_move_raises_exception_when_move_is_invalid(self):
        self.assertRaises(ValueError, self.sut.validate_move, self.BOARD_SIZE ** 2 + 2)
        self.assertRaises(ValueError, self.sut.validate_move, 0)
        self.assertRaises(ValueError, self.sut.play_move, 'w', self.player_x)

    def test_validate_move_returns_true_for_valid_values(self):
        for i in range(1, self.BOARD_SIZE ** 2 + 1):
            self.assertTrue(self.sut.validate_move(i))

    def test_convert_position_to_coord_returns_correct_coordinates(self):
        pos = 1
        for i in range(self.BOARD_SIZE):
            for x in range(self.BOARD_SIZE):
                self.assertEqual(self.sut.convert_pos_to_coord(pos), (i,x))
                pos += 1

    def test_check_winner_returns_player_if_winner(self):

        for i in range(self.BOARD_SIZE):
            test_board = Board(self.create_winning_board_for_row(i, self.player_x))
            self.assertEqual(test_board.get_winner(), self.player_x)

        for i in range(self.BOARD_SIZE):
            test_board = Board(self.create_winning_board_for_col(i, self.player_x))
            self.assertEqual(test_board.get_winner(), self.player_x)

        # left diagonal
        test_board = Board(self.create_winning_board_for_diagonal(self.player_x))
        self.assertEqual(test_board.get_winner(), self.player_x)

        # right diagonal
        test_board = Board(self.create_winning_board_for_diagonal(self.player_x, False))
        self.assertEqual(test_board.get_winner(), self.player_x)

        self.sut.init_board(self.BOARD_SIZE)

    def create_winning_board_for_row(self, row, player):
        test_board = [[(col * self.BOARD_SIZE + row) + 1 for row in range(self.BOARD_SIZE)] for col in range(self.BOARD_SIZE)]
        for i in range(self.BOARD_SIZE):
            test_board[row][i] = player
        
        return test_board

    def create_winning_board_for_col(self, col, player):
        test_board = [[(col * self.BOARD_SIZE + row) + 1 for row in range(self.BOARD_SIZE)] for col in range(self.BOARD_SIZE)]
        for i in range(self.BOARD_SIZE):
            test_board[i][col] = player
        
        return test_board
    
    def create_winning_board_for_diagonal(self, player, is_left = True):
        test_board = [[(col * self.BOARD_SIZE + row) + 1 for row in range(self.BOARD_SIZE)] for col in range(self.BOARD_SIZE)]
        if is_left:
            for i in range(self.BOARD_SIZE):
                test_board[i][i] = player
        else:
            for i in range(self.BOARD_SIZE):
                test_board[i][self.BOARD_SIZE - i - 1] = player

        return test_board

if __name__ == '__main__':
    unittest.main()
