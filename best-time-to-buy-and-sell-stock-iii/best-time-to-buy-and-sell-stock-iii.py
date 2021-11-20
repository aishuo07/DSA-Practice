class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1, buy2, sell2 = float('-inf'), 0, float('-inf'), 0
        for i in prices:
            sell2 = max(sell2, i+buy2)
            buy2 = max(buy2, sell1-i)
            sell1 = max(sell1, buy1 + i)
            buy1 = max(buy1, -i)
        return sell2