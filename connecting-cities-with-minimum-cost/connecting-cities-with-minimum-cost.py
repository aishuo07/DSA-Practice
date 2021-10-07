class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda x: x[2])
        graph = defaultdict(list)
        for i in connections:
            graph[i[0]].append([i[1], i[2]])
            graph[i[1]].append([i[0], i[2]])
        vis = set()
        h = [[0, 1]]
        cost = 0
        while h and len(vis)<n:
            dis, city = heappop(h)
            if city not in vis:
                vis.add(city)
                cost += dis
                for i in graph[city]:
                    heappush(h, [i[1], i[0]])
        return cost if len(vis) == n else -1