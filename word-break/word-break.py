class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache
        def rec(i):
            if i == n:
                return True
            t = ''
            for j in range(i, n):
                t+=s[j]
                if t in wordDict and rec(j+1):
                    return True
            return False
        return rec(0)
                    