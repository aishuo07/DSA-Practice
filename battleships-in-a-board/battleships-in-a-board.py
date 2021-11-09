class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(i, j):
            board[i][j] = '.'
            for k in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                x, y = i+k[0], j+k[1]
                if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'X':
                    dfs(x, y)
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    count+=1
                    dfs(i, j)
        return count