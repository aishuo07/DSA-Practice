class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic= {}
        for j, i in enumerate(s):
            if i not in dic:
                dic[i] = [j, j]
            else:
                dic[i][1] = max(dic[i][1], j)
        su = 0
        for i in dic:
            se =set()
            for j in range(dic[i][0]+1, dic[i][1]):
                se.add(s[j])
            su += len(se)
        return su