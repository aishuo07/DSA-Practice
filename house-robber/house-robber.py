class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rec(i):
            if i>=len(nums):
                return 0
            return max(nums[i] + rec(i+2), rec(i+1))
        return rec(0)