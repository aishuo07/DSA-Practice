class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        dic = {i:j for j, i in enumerate(nums1)}
        dic1 = {i:j for j, i in enumerate(nums2)}
        mod = 10**9 + 7
        @cache
        def rec(i, flag):
            if flag == 0:
                if i >= len(nums1):
                    return 0
                elif nums1[i] in dic1:
                    return nums1[i] + max(rec(i+1, flag), rec(dic1[nums1[i]]+1, 1))
                else:
                    return nums1[i] + rec(i+1, flag)
            else:
                if i >= len(nums2):
                    return 0
                elif nums2[i] in dic:
                    return nums2[i] + max(rec(i+1, flag), rec(dic[nums2[i]]+1, 0))
                else:
                    return nums2[i] + rec(i+1, flag)
        return max(rec(0, 0), rec(0, 1))%mod