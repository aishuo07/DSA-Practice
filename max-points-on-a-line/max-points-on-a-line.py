class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ma = 0
        for i in range(len(points)):
            d = defaultdict(int)
            for j in range(i, len(points)):
                if points[i] == points[j]:
                    slope = 'sa'
                elif points[i][1] != points[j][1]:
                    slope = ((points[i][0] - points[j][0])/(points[i][1] - points[j][1]))
                else:
                    slope = float('inf')
                d[slope] += 1
            temp = d['sa']
            d['sa'] = 0
            ma = max(ma, max(d.values()) + temp)
        return ma  