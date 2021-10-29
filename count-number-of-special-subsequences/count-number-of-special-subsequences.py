class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        dp = [[-1]*3 for _ in range(len(nums))]
        def rec(i, n):
            if n==-1 or i == -1:
                return 0
            if dp[i][n] != -1:
                return dp[i][n]
            if nums[i] == n == 0:
                dp[i][n] = (1 + 2*rec(i-1, n))%mod
                return dp[i][n]
            if nums[i] == n:
                dp[i][n] = (rec(i-1, n-1) + 2*rec(i-1, n))%mod
                return dp[i][n]
            dp[i][n] = rec(i-1, n)
            return dp[i][n]
        return rec(len(nums)-1, 2)