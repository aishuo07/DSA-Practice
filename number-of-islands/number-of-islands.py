class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            grid[i][j] = '0'
            for k in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0<=i+k[0]<n and 0<=j+k[1]<m and grid[i+k[0]][j+k[1]] == '1':
                    dfs(i+k[0], j+k[1])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count