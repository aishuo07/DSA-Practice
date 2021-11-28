class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        m = float('-inf')
        s = []
        for i in nums[::-1]:
            if i<m:
                return True
            while s and i>s[-1]:
                m = max(m, s.pop())
            s.append(i)
        return False
            