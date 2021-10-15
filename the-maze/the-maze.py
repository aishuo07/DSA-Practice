class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = deque([start])
        n = len(maze)
        m = len(maze[0])
        vis = {}
        vis[(start[0], start[1])] = None
        while q:
            for _ in range(len(q)):
                c = q.popleft()
                if c == destination:
                    return True
                for i in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    k, j = c
                    if 0<=c[0]+i[0]<n and 0<=c[1] + i[1]<m and maze[i[0]+c[0]][i[1]+c[1]]==0:
                        while 0<=k+i[0]<n and 0<=j+i[1]<m and maze[k+i[0]][j+i[1]] ==0:
                            k+=i[0]
                            j+=i[1]
                        if (k, j) not in vis:
                            q.append([k, j])
                            vis[(k, j)] = None
        return False