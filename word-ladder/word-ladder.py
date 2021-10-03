class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}
        wordList.append(beginWord)
        wordList = set(wordList)
        for i in wordList:
            graph[i] = []
        if endWord not in graph:
            return 0
        for i in set(wordList):
            for j in range(len(i)):
                for k in 'abcdefghijklmnopqrstuvwxyz':
                    if i[j] != k:
                        s = i[:j] + k + i[j+1:]
                        if s in graph:
                            graph[i].append(s)
        dis = {i: float('inf') for i in wordList}
        dis[beginWord] = 0
        vis = set()
        h = [[0, beginWord]]
        while h:
            c = heappop(h)
            if c[1] in vis:
                continue
            vis.add(c[1])
            for i in graph[c[1]]:
                if dis[i]>c[0] + 1:
                    dis[i] = c[0] + 1
                    heappush(h, [dis[i], i])
        if dis[endWord] == float('inf'):
            return 0
        return dis[endWord]+1