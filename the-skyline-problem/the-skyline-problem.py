class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        heap = []
        bui = []
        for i in buildings:
            bui.append([i[0], i[2], i[1]])
            bui.append([i[1], 0, i[1]])
        
        bui.sort(key = lambda x:[x[0], -x[1]])
        ans = []
        for i in bui:
            while heap and i[0]>=heap[0][1]:
                heappop(heap)
            if i[1] != 0:
                heappush(heap, [-i[1], i[2]])
            if heap and ((not ans or -heap[0][0]!=ans[-1][1]) and (not ans or ans[-1][0]!=heap[0][1])):
                ans.append([i[0], -heap[0][0]])
            elif not heap and i[0]!=ans[-1][0]:
                ans.append([i[0], 0])
        return ans
                