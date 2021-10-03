class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        graph = defaultdict(list)
        indeg= defaultdict(int)
        arr = []
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indeg[i[0]]+=1
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        while q:
            c = q.popleft()
            arr.append(c)
            for i in graph[c]:
                indeg[i] -=1
                if indeg[i]==0:
                    q.append(i)
        return arr if len(arr) == numCourses else []