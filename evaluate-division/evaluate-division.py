class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        def dfs(i):
            vis[i] = True
            ans = 0
            if i == end and i in graph:
                return 1
            for j in graph[i]:
                if j[0] not in vis:
                    ans = max(ans, dfs(j[0])*j[1])
            return ans
        for i in range(len(equations)):
            graph[equations[i][0]].append([equations[i][1], values[i]])
            graph[equations[i][1]].append([equations[i][0], 1/values[i]])
        ans =[]
        for i in queries:
            end = i[1]
            vis = {}
            c = dfs(i[0])
            
            if c == 0:
                c = -1
            ans.append(c)
        return ans