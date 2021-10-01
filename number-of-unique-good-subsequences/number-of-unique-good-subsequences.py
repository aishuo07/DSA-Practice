class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp = [0, 0]
        z = 0
        for i in binary:
            if i == '0':
                z = 1
            dp[int(i)] = dp[0] +dp[1] + int(i)
        return (sum(dp) + z)%(10**9 + 7)