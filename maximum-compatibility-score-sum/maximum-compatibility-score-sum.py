class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        compat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                c = 0
                for k in range(len(students[i])):
                    if students[i][k] == mentors[j][k]:
                        c+=1
                compat[i][j] = c
        def rec(i, mask2):
            if i == n:
                return 0
            ans = 0
            for j in range(n):
                if (1<<j) & mask2 == 0:
                    ans = max(ans, compat[i][j] + rec(i+1, mask2 | 1<<j))
            return ans
        return rec(0, 0)