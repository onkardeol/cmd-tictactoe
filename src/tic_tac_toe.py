from .board import Board
from .player import Player

class TicTacToe:

    PLAYER_X = Player('X')
    PLAYER_O = Player('O')
    player_turn = None
    board = None
    winner = None

    def __init__(self):
        self.player_turn = self.PLAYER_X
        self.board = Board()
        self.winner = None

    def start_game(self):
        while self.winner is None and self.board.num_available_moves > 0:
            self.board.print_board()
            self.get_player_move(self.player_turn)
            self.winner = self.board.get_winner()
            self.swap_turns()
        self.print_winner(self.winner)


    def get_player_move(self, player):
        move_played = False
        while not move_played:
            move = input(f"Player {player.name}, please enter your move: ")
            try:
                move_played = self.board.play_move(move, player)
            except ValueError as error:
                print(error) 

    def print_winner(self, winner):
        self.board.print_board()
        if self.winner is None: 
            print("Draw!")
        else:
            print(f"Player {self.winner.name} has won!")

    def swap_turns(self):
        self.player_turn = self.PLAYER_X if self.player_turn == self.PLAYER_O else self.PLAYER_O
