class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0]*(2*(n-1)+1)
        count = {i:2 for i in range(1, n+1)}
        vis = [0]*(n+1)
        count[1] = 1
        def rec(i):
            if i == 2*(n-1) + 1:
                return True
            if arr[i]!=0:
                return rec(i+1)
            for j in range(n, 0, -1):
                if vis[j] or (i+j>=2*(n-1) + 1 or arr[i+j]!=0) and j!=1:
                    continue
                vis[j] = 1
                arr[i] = j
                if j!=1:
                    arr[i+j] = j
                if rec(i+1):
                    return True
                arr[i] = 0
                vis[j] = 0
                arr[i] = 0
                if j!=1:
                    arr[i+j] = 0
            return False
        rec(0)
        return arr
                    