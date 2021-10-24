class Solution:
    def trap(self, arr: List[int]) -> int:
        ans = 0
        l,  r = 0, len(arr)-1
        maxl = 0
        maxr = 0
        while l<=r:
            if maxl<maxr:
                maxl = max(maxl, arr[l])
                ans += maxl - arr[l]
                l+=1
            else:
                maxr = max(maxr, arr[r])
                ans += maxr - arr[r]
                r-=1
        return ans
                