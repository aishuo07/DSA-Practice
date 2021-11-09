class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        def exchange(row, y, y1):
            while y<y1:
                matrix[row][y], matrix[y][n-row-1], matrix[n-row-1][n-y-1], matrix[n-y-1][row] = matrix[n-y-1][row], matrix[row][y], matrix[y][n-row-1], matrix[n-row-1][n-y-1]
                y+=1
        for i in range(n//2):
            exchange(i, i, n-i-1)
        return matrix