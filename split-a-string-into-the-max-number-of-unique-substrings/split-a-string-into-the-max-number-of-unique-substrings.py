class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def rec(i, t):
            if i>=len(s):
                return 0
            ans = 0
            for j in range(i+1, len(s)+1):
                if s[i:j] not in t:
                    t.add(s[i:j])
                    ans = max(ans, 1+rec(j, t))
                    t.remove(s[i:j])
            return ans
        return rec(0, set())