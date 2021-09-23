class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s = 0
        nums.sort()
        su = sum(nums)
        i = len(nums)-1
        while su-s>=s:
            s += nums[i]
            i-=1
        return nums[i+1:][::-1]