class Solution:
    def subsetsWithDup(self, nums):
        ans = set()
        nums.sort()
        def rec(i, temp):
            if i == len(nums):
                if temp[:-1] not in ans:
                    ans.add(temp[:-1])
                    
                return 
            rec(i+1, temp + str(nums[i]) + ' ')
            rec(i+1, temp)
        rec(0, '')
        return [i.split(' ') for i in ans]
        