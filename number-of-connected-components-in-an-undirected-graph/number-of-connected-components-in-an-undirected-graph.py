class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        vis = set()
        count = 0
        def dfs(i):
            vis.add(i)
            for j in graph[i]:
                if j not in vis:
                    dfs(j)
    
        for i in range(n):
            if i not in vis:
                dfs(i)
                count+=1
        return count