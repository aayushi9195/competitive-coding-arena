class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        ans = 0
      
        # Hash map to store frequency of prefix sums.
        # prefix_sum[s] = number of times prefix sum 's' has occurred.
        # Initialize with {0: 1} to handle cases where a prefix sum itself equals k.
        # This means we have 1 array with sum 0, init value
        prefix_sum = {0: 1} 

        for i, num in enumerate(nums):
            count += num
            # Check if there exists a prefix sum such that:
            # current_sum - previous_sum = k
            if count-k in prefix_sum:
                # If such a prefix sum exists, add its frequency to the answer.
                # This accounts for all subarrays ending at current index that sum to k.
                ans += prefix_sum[count-k]
            # Update the frequency of the current prefix sum
            # (i.e., how many times this sum has been seen so far)
            prefix_sum[count] = prefix_sum.get(count, 0) + 1

        # Return the total count of valid subarrays
        return ans

'''
Summary of Core Difference between this and the last question
Leetcode question         525 (Longest)	                          560 (Count)
Local file                contiguous_array.py                     (self)
What to find	            Longest subarray with sum = 0	          Total subarrays with sum = k
What to store	            First index where a sum was seen	      Count of times a sum was seen
When to update map	      Only if count not seen before	          Always: increment prefix_sum[count]
Why store only 1 index?	  Want longest subarray (earliest start)	Not needed — we want all matches

'''
