class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.antidiag = 0

    def move(self, row: int, col: int, player: int) -> int:
        curr_player = 1 if player == 1 else -1

        self.rows[row] += curr_player
        self.cols[col] += curr_player
        if row == col:
            self.diag += curr_player
        if col == (len(self.rows) - 1 - row):
            self.antidiag += curr_player
        
        n = len(self.rows)

        if (abs(self.rows[row]) == n or
        abs(self.cols[col]) == n or
        abs(self.diag) == n or
        abs(self.antidiag) == n):
            return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
