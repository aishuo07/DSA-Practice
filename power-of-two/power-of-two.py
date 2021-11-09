class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = 0
        if n<0:
            return False
        while n:
            if n&1:
                c+=1
            n //= 2
        return True if c==1 else False