class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums.sort()
        h = []
        ma = 0
        for i in nums:
            if i&1:
                ma = max(ma, i*2)
                heappush(h, -i*2)
            else:
                ma = max(ma, i)
                heappush(h, -i)
        res = float('inf')
        mi = -max(h)
        while True:
            c = -heappop(h)
            res = min(res, c-mi)
            if c&1==0:
                mi = min(mi, c//2)
                heappush(h, -(c//2))
            else:
                break
        return res