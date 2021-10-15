class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [0]*m
        s = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[j] += 1
                    s = max(s, 1)
                else:
                    dp[j] = 0
            st = []
            nsr = [0]*m
            for i in range(m-1, -1, -1):
                while st and dp[st[-1]]>=dp[i]:
                    st.pop()
                if st:
                    nsr[i] = st[-1]
                else:
                    nsr[i] = m
                st.append(i)
            st = []
            nsl = [0]*m
            for i in range(m):
                while st and dp[st[-1]]>=dp[i]:
                    st.pop()
                if st:
                    nsl[i] = st[-1]
                else:
                    nsl[i] = -1
                st.append(i)
            print(dp, nsr, nsl)
            for i in range(m):
                s = max(s, min(dp[i], nsr[i]-nsl[i]-1)**2)
        return s