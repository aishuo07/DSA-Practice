class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        j = 0
        h = []
        c = 0
        for i in range(1, 10**5 + 1):
            while j<len(events) and events[j][0] == i:
                heappush(h, events[j][1])
                j+=1
            while h and h[0]<i:
                heappop(h)
            if h:
                heappop(h)
                c+=1
        return c