class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
        q = deque()
        if grid[0][0] == 1:
            return -1
        q.append([0, 0])
        n = len(grid)
        vis = [[0]*n for _ in range(n)]
        count = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if i == n-1 and j == n-1:
                    return count+1
                for k in dirs:
                    if 0<=i+k[0]<n and 0<=j+k[1]<n and grid[i+k[0]][j+k[1]]==0 and vis[i+k[0]][j+k[1]] == 0:
                        q.append([i+k[0], j+k[1]])
                        vis[i+k[0]][j+k[1]] = 1
            count+=1
        return -1