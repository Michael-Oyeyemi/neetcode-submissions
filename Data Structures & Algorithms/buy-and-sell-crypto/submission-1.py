class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        highest = 0
        while p2 < len(prices):
            if prices[p1] >= prices[p2]:
                p1 = p2
            else:
                profit = prices[p2] - prices[p1]
                highest = max(highest, profit)
            p2 += 1
        
        return highest