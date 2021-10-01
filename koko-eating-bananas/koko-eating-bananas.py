class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        def rec(m):
            s = 0
            for i in piles:
                s+=ceil(i/m)
            if s<=h:
                return True
            return False
        l, r = 1, max(piles)
        while l<=r:
            mid = (l+r)//2
            if not rec(mid):
                l = mid+1
            else:
                r = mid-1
        return l