class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ma = 0
        s = 0
        for i in values:
            ma = max(ma, i + s)
            s = max(s, i)
            s-=1
        return ma