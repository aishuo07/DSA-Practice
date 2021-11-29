class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        dic = defaultdict(set)
        for i in allowed:
            dic[i[:2]].add(i[-1])
        def rec(s, i, t):
            if len(s) == 1:
                return True
            if i>=len(s)-1:
                return rec(t, 0, '')
            ans = False
            for j in dic[s[i] + s[i+1]]:
                if rec(s, i+1, t+j):
                    return True
            return False
        return rec(bottom, 0, '')