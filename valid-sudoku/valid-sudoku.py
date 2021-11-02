class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isvalid(i, j, k):
            if board[i][j] == '.':
                return True
            for l in range(9):
                if (board[l][j] == k and l!=i) or (board[i][l] == k and l!=j):
                    return False
            for l in range((i//3)*3, (i//3 +1)*3):
                for m in range((j//3)*3, (j//3 +1)*3):
                    if board[l][m] == k and l !=i and j!=m:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if not isvalid(i, j, board[i][j]):
                    return False
        return True