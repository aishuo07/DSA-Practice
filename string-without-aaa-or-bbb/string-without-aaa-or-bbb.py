class Solution:
    def strWithout3a3b(self, a, b, A = 'a', B = 'b'):
        if a<b:
            return self.strWithout3a3b(b, a,'b','a')
        s = ''
        while a:
            s+= A
            a-=1
            if a>b: 
                s+=A
                a-=1
            if b>0:
                s+=B
                b-=1
        return s