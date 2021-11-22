class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i = n-1
        j = 0
        while True:
            c = matrix[i][j]
            l = i
            r = j
            while l<n and r<m:
                if c!=matrix[l][r]:
                    return False
                l+=1
                r+=1
            if i!=0:
                i-=1
            else:
                j+=1
            if j == m:
                break
        return True