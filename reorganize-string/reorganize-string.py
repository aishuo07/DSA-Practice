class Solution:
    def reorganizeString(self, s: str) -> str:
        c  = Counter(s)
        ma = max(c.values())
        if ma>(len(s)+1)//2:
            return ''
        res = ''
        arr = ['']*len(s)
        j = 0
        l = sorted([[i, j] for j, i in c.items()])
        for i in l[::-1]:
            for k in range(i[0]):
                while j<len(s) and arr[j] != '':
                    j+=1
                arr[j] = i[1]
                j = (j+2)%len(s)
        return ''.join(arr)
                