class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        def dfs(i, temp):
            if i == len(s):
                ans.append(' '.join(temp))
            c = ''
            for j in range(i, len(s)):
                c+=s[j]
                if c in wordDict:
                    dfs(j+1, temp + [c])
        dfs(0, [])
        return ans