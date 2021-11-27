class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        i = j = carry = 0
        res = ''
        while i<len(a) and i<len(b):
            s = int(a[i]) + int(b[i]) + carry
            if s == 3:
                res += '1'
                carry = 1
            elif s == 2:
                res += '0'
                carry = 1
            else:
                res += str(s)
                carry = 0
            i+=1
        while i<len(a):
            s = int(a[i]) + carry
            if s == 2:
                res += '0'
                carry = 1
            else:
                res += str(s)
                carry = 0
            i+=1
        while i<len(b):
            s = int(b[i]) + carry
            if s == 2:
                res += '0'
                carry = 1
            else:
                res += str(s)
                carry = 0
            i+=1
        if carry:
            res += str(carry)
        return res[::-1]