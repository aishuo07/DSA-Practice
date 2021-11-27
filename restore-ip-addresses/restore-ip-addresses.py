class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def rec(i, temp, c):
            tmp = ''
            if i >= len(s) and c==4:
                ans.append(temp[1:])
            if i>=len(s) or c>4:
                return 
            for j in range(i, min(len(s), i+3)):
                tmp += s[j]
                if len(tmp)==1 or (tmp[0] != '0' and -1<int(tmp)<256):
                    rec(j+1, temp + "." + tmp, c + 1)
        
            
        rec(0, '', 0)
        return ans