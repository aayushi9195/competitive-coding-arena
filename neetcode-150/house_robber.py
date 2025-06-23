class Solution:
    # Time: O(N)
    # Space: O(N)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        # If there is only 1 house, robbing that will give max profit.
        dp[0] = nums[0]
        # If there are 2 houses, as we cannot rob both, we have to pick the max value.
        dp[1] = max(nums[0], nums[1])
        # If there are 3 or more houses, take the max of profit achieved by robbing and not the robbing current house i.e. rob i-2th house and this house OR rob i-1th house.
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        # At every point we compute the max at that point. So in the end return the output at the last element of the dp array to get max profit for all houses.
        return dp[len(nums) - 1]
        
