class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums = Counter([i+j for i in nums1 for j in nums2])
        return sum(nums[-i-j] for i in nums3 for j in nums4)