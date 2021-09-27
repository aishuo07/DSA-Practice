class Solution:
    def numberOfMatches(self, n: int) -> int:
        s = 0
        while n>1:
            s += n//2
            n = (n+1)//2
        return s