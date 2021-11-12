class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q, n, m = deque(), len(grid), len(grid[0])
        q.append([0, 0, k, 0])
        vis = {(0, 0, k):None}
        while q:
            c = q.popleft()
            if c[0] == n-1 and c[1] == m-1:
                return c[-1]
            for i in [[0, 1], [-1, 0], [1, 0], [0, -1]]:
                x, y = i[0] + c[0], i[1] + c[1]
                if 0<=x<n and 0<=y<m:
                    if grid[x][y] == 1 and c[-2]>0 and (x, y, c[2]-1) not in vis:
                        q.append([x, y, c[2]-1, c[-1] + 1])
                        vis[(x, y, c[2]-1)] = None
                    elif grid[x][y] == 0 and (x, y, c[2]) not in vis:
                        q.append([x, y, c[2], c[-1] + 1])
                        vis[(x, y, c[2])] = None
        return -1