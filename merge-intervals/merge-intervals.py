class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = []
        for i in intervals:
            if prev and prev[-1][0]<=i[0]<=prev[-1][1]:
                prev[-1][1] = max(i[1], prev[-1][1])
            else:
                prev.append(i)
        return prev