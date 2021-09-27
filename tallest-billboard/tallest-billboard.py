class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        s = sum(rods)
        ma = [0]
        dp = defaultdict(int)
        dp[0] = 0
        for i in rods:
            for j, y in list(dp.items()):
                dp[j + i] = max(dp[j+i], y)
                dp[abs(j-i)] = max(dp[abs(j-i)], y + min(i, j))
        return dp[0]