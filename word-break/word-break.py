class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        @cache
        def rec(i):
            if i >= n:
                return True
            t = ''
            ans = False
            for j in range(i, n):
                t += s[j]
                if t in wordDict:
                    ans |= rec(j+1)
            return ans
        return rec(0)