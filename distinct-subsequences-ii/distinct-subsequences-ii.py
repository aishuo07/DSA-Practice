class Solution:
    def distinctSubseqII(self, s: str) -> int:
        se = set()
        dp = [0]*26
        for i in s:
            dp[ord(i)-ord('a')] = sum(dp) + 1
        return (sum(dp))%1000000007