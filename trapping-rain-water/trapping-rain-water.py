class Solution:
    def trap(self, height: List[int]) -> int:
        ma = 0
        n = len(height)
        left = []
        for i in height:
            ma = max(ma, i)
            left.append(ma)
        ans = 0
        ma = 0
        for i in range(len(height)-1, -1, -1):
            ma = max(ma, height[i])
            ans += max(0, min(ma, left[i]) - height[i])
        return ans