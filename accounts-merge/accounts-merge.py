class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = defaultdict(list)
        for j, i in enumerate(accounts):
            for k in i[1:]:
                d[k].append(j)
        def dfs(i):
            arr.append(i)
            vis[i] = None
            for j in d[i]:
                for k in accounts[j][1:]:
                    if k not in vis:
                        dfs(k)
        vis = {}
        res = []
        for i in d.copy():
            if i not in vis:
                arr = []
                dfs(i)
                res.append([accounts[d[i][0]][0]] + sorted(arr))
        return res
                
                    
    