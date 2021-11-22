class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for i in flights:
            graph[i[0]].append([i[1], i[2]])
        heap = []
        dis = [[float('inf') for _ in range(k+1)] for _ in range(n)]
        for i in graph[src]:
            heappush(heap, [i[1], i[0], 1])
            dis[i[0]][0] = i[1]
        vis = set()
        vis.add((src, 0))
        
        while heap:
            c = heappop(heap)
            if (c[1], c[2]) in vis:
                continue
            for i in graph[c[1]]:
                
                if c[2]<=k and (dis[i[0]][c[2]]>c[0] + i[1]):
                    dis[i[0]][c[2]] = c[0] + i[1]
                    heappush(heap, [dis[i[0]][c[2]], i[0], c[2]+1])
            vis.add((c[1], c[2]))
        ans = min([dis[dst][i] for i in range(k+1)])
        return ans if ans != float('inf') else -1
            
            
            
            
        