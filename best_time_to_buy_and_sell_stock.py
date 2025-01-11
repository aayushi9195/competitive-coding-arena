class Solution:

    # Time: O(N)
    # Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        # On the first day we can only buy, not sell. So set this as the starting buy value.
        min_buy  = prices[0]

        # Iterate through the rest of the days
        for i in range(1, len(prices)):
            # At any point, we can either buy or sell. If the price is less than minimum buy so far, then update the min_buy. No point selling here as the profit will go negative.
            if prices[i] < min_buy:
                min_buy = prices[i]
            # If the price is greater than min_buy, then we can sell and update the maximum profit we have seen so far.
            else:
                max_profit = max(max_profit, prices[i] - min_buy)

        # Return the maximum possible profit.
        return max_profit
        
