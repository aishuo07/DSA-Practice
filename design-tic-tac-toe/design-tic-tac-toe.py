class TicTacToe:

    def __init__(self, n: int):
        self.row = [[0, 0] for _ in range(n)]
        self.collumn = [[0, 0] for _ in range(n)]
        self.dia1 = [0, 0]
        self.dia2 = [0, 0]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        def helper():
            if self.row[row][player-1] == self.n or self.collumn[col][player-1]==self.n or self.dia1[player-1] == self.n or self.dia2[player-1] == self.n:
                return player
            return 0
        self.row[row][player-1] += 1
        self.collumn[col][player-1] += 1
        if row == col:
            self.dia1[player-1] += 1
        if row+col == self.n-1:
            self.dia2[player-1] += 1
        return helper()
        