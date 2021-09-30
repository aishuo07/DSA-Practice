class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indeg[i[0]]+=1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        vis = [0]*numCourses
        while q:
            c = q.popleft()
            vis[c] = 1
            for i in graph[c]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        return all(i for i in vis)