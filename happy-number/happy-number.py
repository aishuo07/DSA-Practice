class Solution:
    def isHappy(self, n: int) -> bool:
        def rec(n):
            s = 0
            while n:
                s += (n%10)*(n%10)
                n//=10
            return s
        fast = slow = n
        fast = rec(n)
        while fast != slow and fast!=1:
            slow = rec(slow)
            fast = rec(fast)
            fast = rec(fast)
        if fast == 1:
            return True
        return False
                        