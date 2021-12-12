class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def rec(i, j):
            if j == len(t):
                return 1
            if i>=len(s):
                return 0
            if s[i] == t[j]:
                return rec(i+1, j+1) + rec(i+1, j)
            return rec(i+1, j)
        return rec(0, 0)