class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        m = min(nums)
        m = 1
        while m in s:
            m+=1
        return m