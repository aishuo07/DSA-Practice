class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        n = len(s)
        def rec(i, path):
            if i == n:
                ans.append(path[:-1])
            t = ''
            for j in range(i, n):
                t += s[j]
                if t in wordDict:
                    rec(j+1, path + t + ' ')
        rec(0, '')
        return ans