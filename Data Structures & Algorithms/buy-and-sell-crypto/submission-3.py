class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        prof = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                prof = max(prof, abs(prices[i] - prices[j]))
            else:
                i = j

            j += 1
        return prof
            
