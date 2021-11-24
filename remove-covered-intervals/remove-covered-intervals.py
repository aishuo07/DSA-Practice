class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:[x[0], -x[1]])
        res = []
        for i in intervals:
            if res and res[-1][0]<=i[0]<=i[1]<=res[-1][1]:
                continue
            res.append(i)
        return len(res)