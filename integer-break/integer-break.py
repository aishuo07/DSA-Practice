class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def rec(n, k):
            if n == 0 and k>=2:
                return 1
            if n == 0:
                return 0
            if (n, k if k<2 else 2) in dp:
                return dp[(n, k if k<2 else 2)]
            ma = 0
            for i in range(1, n+1):
                ma = max(ma, i*rec(n-i, k+1))
            dp[(n, k if k<2 else 2)] = ma
            return ma
        return rec(n, 0)