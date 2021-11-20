class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], tar: int) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = float('-inf')
        for i in range(m):
            s = [0]*n
            for j in range(i, m):
                for k in range(n):
                    s[k] += matrix[k][j]
                l = 0
                ind = 0
                arr = [0]
                for k in range(n):
                    l += s[k]
                    ind = bisect.bisect_left(arr, l- tar)
                    if ind<len(arr):            
                        ans = max(ans, l-arr[ind])
                    bisect.insort(arr, l)
        return ans
                    