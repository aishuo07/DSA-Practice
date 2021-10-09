class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        c0 = 0
        c1 = 0
        n = len(s)
        co0 = s.count('0')
        ma = co0
        for i in range(n):
            if s[i] == '0':
                c0+=1
            else:
                c1 += 1
            ma = min(ma, c1+(co0-c0))
        return ma