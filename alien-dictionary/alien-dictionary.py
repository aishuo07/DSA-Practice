class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indeg = defaultdict(int)
        for i in range(1, len(words)):
            for j in range(i):
                flag = False
                for k in range(min(len(words[j]), len(words[i]))):
                    if words[j][k] != words[i][k]:
                        flag = True
                        graph[words[j][k]].add(words[i][k])
                        break
                if not flag and len(words[j])>len(words[i]):
                    return ''
        q = deque()
        allwords = set()
        for i in words:
            allwords|=set(i)
        for i in allwords:
            indeg[i] = 0
        for i in allwords:
            for j in graph[i]:
                indeg[j] +=1
        for i in indeg:
            if indeg[i] == 0:
                q.append(i)
        ans = ''
        print(graph, indeg, q)
        while q:
            c = q.popleft()
            ans += c
            for i in graph[c]:
                indeg[i] -=1
                if indeg[i] == 0:
                    q.append(i)
            
        return ans if len(allwords) == len(ans) else ''