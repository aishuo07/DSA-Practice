class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        h = [[-value, key] for key, value in c.items()]
        heapify(h)
        res = ''
        num, st = 0, ''
        while h:
            a, b = heappop(h)
            res += b
            if num<0:
                heappush(h, [num, st])
            a+=1
            num, st = a, b
        print(res, h)
        return res if len(res) == len(s) else ''