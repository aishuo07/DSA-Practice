class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append([i[1], i[2]])
            graph[i[1]].append([i[0], i[2]])   
        ma = float('inf')
        city = 0
        for i in range(n):
            dis = [float('inf')]*n
            dis[i] = 0
            vis = set()
            h = []
            heappush(h, [0, i])
            while h:
                c = heappop(h)
                if c[1] in vis:
                    continue
                vis.add(c[1])
                for j in graph[c[1]]:
                    if dis[j[0]]>=c[0] + j[1]:
                        dis[j[0]]=c[0] + j[1]
                        heappush(h, [dis[j[0]], j[0]])
            count = -1
            for j in dis:
                if j<=distanceThreshold:
                    count+=1
            if ma>=count:
                ma = count
                city = i
        return city