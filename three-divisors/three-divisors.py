class Solution:
    def isThree(self, n: int) -> bool:
        c = 0
        for i in range(2, int(sqrt(n)+1)):
            if n%i==0:
                if n/i != i or c == 1:
                    return False
                c+=1
                
        return True if c == 1 else False