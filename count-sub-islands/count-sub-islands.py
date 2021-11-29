class Solution:
    def countSubIslands(self, grid1, grid2):
        n, m = len(grid2), len(grid2[0])
        c = 0
        def dfs(i, j):
            if not (grid1[i][j] == grid2[i][j] == 1):
                return False
            grid2[i][j] = 0
            ans = True
            for k in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                x, y = i+k[0], j+k[1]
                if 0<=x<n and 0<=y<m and grid2[x][y] == 1:
                    ans&=dfs(x, y)
            return ans
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        c+=1
        return c