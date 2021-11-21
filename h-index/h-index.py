class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        l, r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            if n-mid>citations[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return n-l