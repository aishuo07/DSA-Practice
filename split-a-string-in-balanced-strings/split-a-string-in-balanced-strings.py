class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        res = 0
        for i in s:
            c+=1 if i == 'L' else -1
            if c ==0:
                res += 1 
        return res