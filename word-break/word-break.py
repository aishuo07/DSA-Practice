class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        @cache
        def rec(i):
            if i == len(s):
                return True
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict and rec(j+1):
                    return True
        return rec(0)
            