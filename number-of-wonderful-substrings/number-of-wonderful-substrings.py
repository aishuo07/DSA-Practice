class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        mask = 0
        ans = 0
        for j in word:
            
            mask ^= 1<<(ord(j)-ord('a'))
            ans += dp[mask]
            for i in range(10):
                ans += dp[mask ^ 1<<i]
            dp[mask] += 1
        return ans