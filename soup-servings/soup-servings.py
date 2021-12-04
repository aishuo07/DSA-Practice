class Solution:
    def soupServings(self, n: int) -> float:
        if n>=4800:
            return 1
        n = (n+24)//25
        @cache
        def rec(a, b):
            if a<=0 and b<=0:
                return 0.5
            if a<=0:
                return 1
            if b<=0:
                return 0
            return (1/4)*(rec(a-4, b)+ rec(a-3, b-1)+ rec(a-2, b-2)+ rec(a-1, b-3))
        return rec(n, n)