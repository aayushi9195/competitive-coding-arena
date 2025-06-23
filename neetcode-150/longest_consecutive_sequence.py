class Solution:

    # Time: O(N)
    # Space: O(N)
    def longestConsecutive(self, nums: List[int]) -> int:

        # Convert list into a set so we can have O(1) lookups
        s = set(nums)
        max_length = 0
        
        for num in nums:
            # Ignore the number if it is not the smallest as no new sequence can start from there eg if 1, 2, 3, 4 is the longest sequence, we only need to check for it starting from 1. If we start from 2, 3 or 4, the resulting sequence will always be smaller. So we can ignore the numbers that are already a part of larger sequence.
            if num - 1 in s:
                continue
            # Start tracking the length from the current starting number
            curr_length = 1
            # Increment it every time we see a consecutive number
            while num + 1 in s:
                curr_length += 1
                num += 1
            # Update the response if we have found a longer sequence    
            max_length = max(max_length, curr_length)

        return max_length
