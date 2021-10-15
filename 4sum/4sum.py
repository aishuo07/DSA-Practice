class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums.sort()
        for i in range(n):
            for j in range(i+1, n):
                l = j+1
                r = n-1
                tar = target - nums[i] - nums[j]
                while l<r:
                    if nums[l] + nums[r]<tar:
                        l+=1
                    else:
                        if nums[l] + nums[r] == tar:
                            ans.add((nums[i], nums[j], nums[l], nums[r]))
                        r-=1
        return ans
                        