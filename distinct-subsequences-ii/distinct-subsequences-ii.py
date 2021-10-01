class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = defaultdict(int)
        mod = 10**9 + 7
        for i in s:
            dp[i] = (sum(dp.values()) + 1)%mod
        return sum(dp.values())%mod