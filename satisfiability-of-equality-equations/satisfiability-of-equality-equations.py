class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {i:i for i in 'abcdefghijklmnopqrstuvwxyz'}
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        for i in equations:
            if i[1] == '=':
                parent[find(i[0])] = find(i[3])
        return not any(i for i in equations if i[1] == '!' and find(i[0]) == find(i[3]))