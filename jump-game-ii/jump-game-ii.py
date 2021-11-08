class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        j = 0
        c = 0
        ma = 0
        if len(nums) == 1:
            return 0
        while True:
            while i<=j:
                ma = max(ma, i+nums[i]) 
                i+=1
            j = ma
            c+=1
            if j >= len(nums)-1:
                return c
            