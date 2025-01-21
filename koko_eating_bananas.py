class Solution:

    # Time: O(N*logM) where N is len(piles) and M is len(tallest pile).
    # Space: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def cannot_finish(eating_rate):
            time_taken = 0
            # Divide the number of bananas with eating rate to get the number of hours needed to finish eating that pile. Take the ceiling of the value eg. for 3 bananas at the rate of 2 she will need 2 hours to eat 3.
            for pile in piles:
                time_taken += pile // eating_rate
                if pile % eating_rate != 0:
                    time_taken += 1
            # If the total time needed to finish all bananas goes beyond h, then this eating_rate is too slow.
            return time_taken > h

        # Koko will eat minimum 1 banana in an hour.
        min_rate = 1
        # If Koko eats the largest pile in an hour, then she can eat any other pile also in an hour. So the maximum eating rate can be length of the largest pile. Eating_rate does not need to be more than that.
        max_rate = max(piles)
        # Initialize answer to maximum possible rate.
        res = max_rate

        # Instead of trying all rates linearly, use binary search to reduce time complexity from M to log M.
        while min_rate <= max_rate:
            mid_rate = int(min_rate + (max_rate - min_rate) / 2)
            # If Koko cannot finish eating all bananas with current rate, it means the speed/rate need to increase.
            if cannot_finish(mid_rate):
                min_rate = mid_rate + 1
            # If she can, then update the response but don't break yet because there may be a smaller rate that Koko can use to eat all the bananas in the given time.
            else:
                res = mid_rate
                max_rate = mid_rate - 1
        
        return res
        
