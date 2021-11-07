class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid + 1
            else:
                r = mid-1
        if l>=len(nums) or nums[l] != target:
            return [-1, -1]
        else:
            ans = [l]
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]<=target:
                    l = mid + 1
                else:
                    r = mid-1
            ans.append(l-1)
            return ans
