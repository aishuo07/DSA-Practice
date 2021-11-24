class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j] = 0
            for k in [[0, 1], [1, 0], [-1,0], [0, -1]]:
                x, y = i+k[0], j+k[1]
                if 0<=x<n and 0<=y<m and grid[x][y] == '1':
                    dfs(x, y)
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans