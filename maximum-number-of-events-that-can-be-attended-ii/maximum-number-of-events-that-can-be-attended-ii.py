class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        @cache
        def rec(i, k):
            
            if k == 0 or i >= len(events):
                return 0
            return max(events[i][2] + rec(bisect.bisect(events, [events[i][1]+1, 0, 0]), k-1), rec(i+1, k))
        return rec(0, k)