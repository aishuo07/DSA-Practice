class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def rec(i, s):
            if s == 0:
                return 0
            if i == len(coins):
                return float('inf')
            ans = float('inf')
            if s>=coins[i]:
                ans = min(ans, 1+ rec(i, s-coins[i]))
            ans = min(ans, rec(i+1, s))
            return ans
        c = rec(0, amount)
        if c == float('inf'):
            return -1
        return c