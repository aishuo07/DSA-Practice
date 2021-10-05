class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = Counter(i+j for i in nums1 for j in nums2)
        count = 0
        for i in nums3:
            for j in nums4: 
                if -(i+j) in dic: count+=dic[-(i+j)]
        return count