class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        arr = [[0, float('-inf')] for _ in range(k+1)]

        for i in prices:
            for j in range(k):
                arr[j][0] = max(arr[j][0], i+arr[j][1])
                arr[j][1] = max(arr[j][1], arr[j-1][0]-i)
        
        return max([i[0] for i in arr])