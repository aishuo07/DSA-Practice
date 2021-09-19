class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        arr =[]
        s = set()
        for i in range(1, n):
            for j in range(i+1, n+1):
                if i/j not in s:
                    s.add(i/j)
                    arr.append(str(i) + '/' + str(j))
        return arr