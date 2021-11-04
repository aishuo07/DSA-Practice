class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def valid(i, j, k):
            for l in range(9):
                if board[i][l] == k or board[l][j] == k:
                    return False
            for l in range((i//3)*3, (i//3 + 1)*3):
                for m in range((j//3)*3, (j//3 + 1)*3):
                    if board[l][m] == k:
                        return False
            return True
        def rec(i, j):
            if i == 9 and j == 0:
                return True
            if j == 9:
                return rec(i+1, 0)
            if board[i][j] !='.':
                return rec(i, j+1)
            for k in range(1, 10):
                if valid(i, j, str(k)):
                    board[i][j] = str(k)
                    if rec(i, j+1):
                        return True
                    board[i][j] = '.'
            return False
        rec(0, 0)