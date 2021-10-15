class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        vis = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and ((0<=i+1<n and grid[i+1][j] == 1) or (0<=i-1<n and grid[i-1][j] == 1) or (0<=j+1<m and grid[i][j+1] == 1) or (0<=j-1<n and grid[i][j-1] == 1)):
                    q.append([i, j, 1])
                    vis[(i,j)] = None
        ma = -1
        while q:
            for _ in range(len(q)):
                c, d, dis = q.popleft()
                ma = max(ma, dis)
                for k in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
                    i, j = c+k[0], d+k[1]
                    if 0<=i<n and 0<=j<m and grid[i][j] == 0 and (i, j) not in vis:
                        q.append([i, j, dis+1])
                        vis[(i, j)] = None
        return ma