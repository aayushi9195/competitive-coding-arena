class Solution:
    # Time: O(N)
    # Space: O(N)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Because we need to reach the end i.e. one position after the last element of cost array
        dp = [0] * (n+1)
        # As we can start from 0 or 1, the min cost to reach 0 and 1 is 0. So we start calculating cost from position 2 till the end.
        for i in range(2, n+1):
            # At every step, the min cost is the cost at i-1 or i-2th step plus the cost incurred coming from i-1 or i-2 to i.
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        # Return the cost incurred to reach the end i.e. element after the last element of cost array
        return dp[n]
        
