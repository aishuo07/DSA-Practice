class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = j = k
        ma = 0
        mi = nums[k]
        print(len(nums))
        while i>=0 and j<len(nums):
            ma = max(ma, (j-i+1)*mi)
            if (i<=0 and j<len(nums)-1) or (i>0 and j<len(nums)-1 and nums[i-1]<nums[j+1]):
                mi = min(mi, nums[j+1])
                j+=1
            else:
                mi = min(mi, nums[i-1])
                i-=1
        return ma