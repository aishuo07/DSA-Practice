class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        c0 = 0
        c1 = 0
        for i in s:
            if i == '1':
                c1+=1
            else:
                c0 = min(c0+1, c1)
        return c0