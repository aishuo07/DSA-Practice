class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:[x[1], x[0]])
        first, last = -1, -1
        m = 0
        for i in intervals:
            if first>=i[0]:
                continue
            elif last>=i[0]:
                if last == i[1]:
                    first = last-1
                else:
                    first = last
                    last = i[1]
                m+=1
            else:
                first, last = i[1]-1, i[1]
                m+=2
        return m