class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        r = n-1
        while l<=r:
            mid = (l+r)//2
            if n-mid>citations[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return n-l