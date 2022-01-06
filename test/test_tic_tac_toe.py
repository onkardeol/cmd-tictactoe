import unittest
from src.tic_tac_toe import TicTacToe
from src.player import Player

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.sut = TicTacToe()
        self.player_x = Player('X')
        self.player_o = Player('O')

    def test_swap_turn_returns_the_opposite_player(self):
        self.sut.swap_turns()
        self.assertEqual(self.sut.player_turn, self.player_o)
        self.sut.swap_turns()
        self.assertEqual(self.sut.player_turn, self.player_x)


if __name__ == '__main__':
    unittest.main()
