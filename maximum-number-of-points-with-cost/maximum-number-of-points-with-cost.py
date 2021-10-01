class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
            dp = points[0][:]
            n, m = len(points), len(points[0])
            for i in range(1, n):
                new = [0]*m
                ma = 0
                for j in range(m):
                    ma = max(ma, dp[j])
                    new[j] = ma
                    ma -= 1
                ma = 0
                for j in range(m-1, -1, -1):
                    ma = max(ma, dp[j])
                    new[j] = max(new[j], ma)
                    ma -= 1
                dp = [l+m for l, m in zip(new, points[i])]
            return max(dp)
                        