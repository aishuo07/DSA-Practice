class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        prev = 0
        m = 0
        for i in horizontalCuts:
            m = max(m, i-prev)
            prev = i
        m = max(m, h-prev)
        prev = 0
        
        ma = 0
        for i in verticalCuts:
            ma = max(ma, i-prev)
            prev = i
        ma = max(ma, w-prev)
        return (ma*m)%(10**9 + 7)
               