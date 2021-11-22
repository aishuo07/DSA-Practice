class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        flag= False
        ans = []
        s = ''
        for i in source:
            if not flag:
                s = ''
            j = 0
            while j<len(i):
                if i[j:j+2] == '//' and not flag:
                    break
                elif i[j:j+2] == '/*' and not flag:
                    flag = True
                    j+=1
                elif flag and i[j:j+2] == '*/':
                    flag = False
                    j+=1   
                elif not flag:
                    s += i[j]
                j+=1
            if s and not flag:
                ans.append(s)
        return ans