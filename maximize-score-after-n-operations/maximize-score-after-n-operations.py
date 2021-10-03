class Solution:
    def maxScore(self, nums: List[int]) -> int:
        arr = []
        from math import gcd
        s = []
        for i in nums:
            s+=['0']
        dp = {}
        def rec(s, ind):
            ans = 0
            c = ''.join(s[:])
            if (c, ind) in dp:
                return dp[(c, ind)]
            for i in range(len(s)):
                for j in range(len(s)):
                    if i!=j and s[i]!='1' and s[j]!='1':                    
                        s[i] = '1'
                        s[j] = '1'
                        ans = max(ans, ind*gcd(nums[i], nums[j]) + rec(s, ind+1))
                        s[i] = '0'
                        s[j] = '0'
            dp[(c, ind)] = ans
            return ans
        return rec(s, 1)