class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for day in range(1,len(prices)):
            if prices[day]<buy:
            # if prices[day-1]>prices[day]:
                buy=prices[day]
            profit=max(profit,prices[day]-buy)
        return profit