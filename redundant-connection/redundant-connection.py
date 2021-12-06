class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(a):
            if par[a] == a:
                return a
            par[a] = find(par[a])
            return par[a]
        def union(a, b):
            c, d = find(a), find(b)
            if c == d:
                return False
            par[c] = d
            return True
        par = {}
        for i in edges:
            if i[0] not in par:
                par[i[0]] = i[0]
            if i[1] not in par:
                par[i[1]] = i[1]
            if not union(i[0], i[1]):
                return i
            