class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        ans = False
        vis = [[0]*m for _ in range(n)]
        def dfs(i, j, k):
            a = False
            vis[i][j] = 1
            if k == len(word):
                return True
            
            for l in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0<=i+l[0]<n and 0<=j+l[1]<m and board[i+l[0]][j+l[1]] == word[k] and vis[i+l[0]][j+l[1]]==0:
                    a|=dfs(i+l[0], j+l[1], k+1)
            vis[i][j] = False
            return a
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    ans|=dfs(i, j, 1)
        return ans