class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        c=0
        while len(sticks)>1:
            ans = heappop(sticks)+heappop(sticks)
            heappush(sticks, ans)
            c+=ans
        return c