class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def rec(i, temp):
            if i == len(s):
                ans.append(temp.rstrip(' '))
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    rec(j+1, temp + s[i:j+1] + ' ')
            
        rec(0, '')
        return ans