class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)] 
        self.n = n

    def check_row(self, row, player):
        for col in range(self.n):
            if self.board[row][col] != player:
                return False
        return True

    def check_col(self, col, player):
        for row in range(self.n):
            if self.board[row][col] != player:
                return False
        return True
    
    def check_dia(self, player):
        for row in range(self.n):
            if self.board[row][row] != player:
                return False
        return True

    def check_antidia(self, player):
        for row in range(self.n):
            if self.board[row][self.n - row - 1] != player:
                return False
        return True

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if (self.check_row(row,player) or self.check_col(col, player) or (row == col and self.check_dia(player)) or (row == self.n - col - 1 and self.check_antidia(player))):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)