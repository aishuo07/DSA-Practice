class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        s =set()
        count= 0
        def dfs(i):
            s.add(i)
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and j not in s:
                    dfs(j)
            
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i not in s:
                    dfs(i)
                    count+=1
        return count