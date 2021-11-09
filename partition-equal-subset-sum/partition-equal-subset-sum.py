class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        su = sum(nums)
        if su&1:
            return False
        @cache
        def rec(i, s):
            if s == 0:
                return True
            if i == len(nums):
                return False
            return rec(i+1, s-nums[i]) or rec(i+1, s)
        return rec(0, su//2)