class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        def dfs(i, j):
            board[i][j] = '1'
            for k in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0<=i+k[0]<n and 0<=j+k[1]<m and board[i+k[0]][j+k[1]] == 'O':
                    dfs(i+k[0], j+k[1])
        for i in range(m):
            if board[0][i] == 'O':
                dfs(0, i)
        for i in range(m):
            if board[n-1][i] == 'O':
                dfs(n-1, i)
        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
        for i in range(n):
            if board[i][m-1] == 'O':
                dfs(i, m-1)
        for i in range(n):
            for j in range(m):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board
                
        