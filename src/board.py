class Board:

    __BOARD_SIZE = 3
    board = None
    num_available_moves = None

    def __init__(self, board = None):
        if board is not None:
            self.board = board
        else:
            self.board = self.init_board(self.__BOARD_SIZE)
        self.num_available_moves = self.__BOARD_SIZE ** 2

    @staticmethod
    def init_board(board_size):
        return [[(col * board_size + row) + 1 for row in range(board_size)] for col in range(board_size)]

    def print_board(self):
        print('\n')
        for section in range(self.__BOARD_SIZE):
            print(' | '.join(map(self.elem_mapper, self.board[section])), end='')
            print("\n---------") if section != self.__BOARD_SIZE - 1 else print('\n')

    @staticmethod
    def elem_mapper(elem):
        if isinstance(elem, int):
            return str(elem)
        
        return elem.name

    def play_move(self, position, player):
        if self.validate_move(position):
            coord = self.convert_pos_to_coord(int(position))
            self.board[coord[0]][coord[1]] = player
            self.num_available_moves -= 1
            return True

        return False

    def validate_move(self, position):
        try:
            pos= int(position)
        except:
            raise ValueError(f"Invalid move, Select a number from 1 to {self.__BOARD_SIZE ** 2}")

        lenBoardSize = self.__BOARD_SIZE ** 2
        if pos > lenBoardSize or pos < 1:
            raise ValueError(f"Invalid move, Select a number from 1 to {lenBoardSize}")
        
        coord = self.convert_pos_to_coord(pos)
        value_at_board_position = self.board[coord[0]][coord[1]]
        if not isinstance(value_at_board_position, int):
            raise ValueError(f"Invalid move, this position is occupied")
        
        return True

    def convert_pos_to_coord(self, pos):
        position = pos - 1
        row = position // self.__BOARD_SIZE
        col = position - row * self.__BOARD_SIZE

        return (row, col)

    def get_winner(self):
        diagonalWinner = self.get_winner_diagonals()
        if diagonalWinner is not None: return diagonalWinner

        rowWinner = self.get_winner_rows()
        if rowWinner is not None: return rowWinner
        
        colWinner = self.get_winner_cols()
        if colWinner is not None: return colWinner

        return None

    def get_winner_diagonals(self):
        leftDiagonalSet = set([self.board[i][i] for i in range(self.__BOARD_SIZE)])
        rightDiagonalSet = set([self.board[i][self.__BOARD_SIZE - i - 1] for i in range(self.__BOARD_SIZE)])

        if len(leftDiagonalSet) == 1:
            return leftDiagonalSet.pop()
        
        if len(rightDiagonalSet) == 1:
            return rightDiagonalSet.pop()

        return None

    def get_winner_rows(self):
        for row in self.board:
            rowSet = set(row)
            if len(rowSet) == 1:
                return rowSet.pop()
        
        return None

    def get_winner_cols(self):
        for col in zip(*self.board):
            colSet = set(col)
            if len(colSet) == 1:
                return colSet.pop()

        return None