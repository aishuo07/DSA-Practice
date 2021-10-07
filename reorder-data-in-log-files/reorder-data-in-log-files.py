class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ar = []
        h = []
        for i in logs:
            c = i.split(' ')
            if c[1][0].isdigit():
                ar.append(i)
            else:
                heappush(h, [' '.join(c[1:]), c[0]])
        c = []
        while len(h):
            d = heappop(h)
            c.append(d[1]+" "+ d[0])
        return c+ar