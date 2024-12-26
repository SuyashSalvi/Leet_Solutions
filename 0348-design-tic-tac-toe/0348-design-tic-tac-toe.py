class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.dia = 0
        self.antidia = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        cur_player = 1 if player == 1 else -1
        self.rows[row] += cur_player
        self.cols[col] += cur_player

        if row == col:
            self.dia += cur_player
        if col == self.n - row - 1:
            self.antidia += cur_player

        if (abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.dia) == self.n or abs(self.antidia) == self.n):
            return player

        return 0    


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)