class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = [0]
        j = 1
        for i in range(n-1, -1, -1):
            if j&1:
                arr += board[i]
            else:
                arr += board[i][::-1]
            j+=1
        q = deque([1])
        sq = n*n
        dp = [0]*(sq+1)
        count = 0
        while q:
            for _ in range(len(q)):
                c = q.popleft()
                if c == sq:
                    return count
                for i in range(c+1, min(c+7, sq+1)):
                    if arr[i] == -1 and dp[i]==0:
                        dp[i] = 1
                        q.append(i)
                    elif dp[arr[i]]==0 and arr[i] != -1:
                        q.append(arr[i])
                        dp[arr[i]] = 1
            count += 1
        return -1