class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [0]*len(points[0])
        for i in points:
            ma = 0
            new = [0]*len(points[0])
            for j in range(len(points[0])):
                ma = max(ma, dp[j])
                new[j] = ma + i[j]
                ma -= 1
            ma = 0
            for j in range(len(points[0])-1, -1, -1):
                ma = max(ma, dp[j])
                new[j] = max(new[j] , ma + i[j])
                ma -= 1
            dp = new[:]
        return max(dp)