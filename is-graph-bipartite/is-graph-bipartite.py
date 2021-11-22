class Solution:
    def isBipartite(self, grap: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for j, i in enumerate(grap):
            graph[j] = i[:]
        def dfs(i, color):
            if i not in vis:
                vis[i] = color
            ans = True
            for j in graph[i]:
                if j not in vis:
                    ans&=dfs(j, not color)
                elif vis[j]==vis[i]:
                    return False
            return ans
        vis = {}
        ans = True
        for i in range(len(grap)):
            if i not in vis:
                ans &= dfs(i, True)
        return ans