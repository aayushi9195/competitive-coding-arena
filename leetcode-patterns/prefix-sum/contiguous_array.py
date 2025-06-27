'''
This solution's time complexity is O(n^2), works if the input size is small.
Core idea: Iterate through all subarrays and at every position store the number of zeros and ones in a tuple. Where the numbers are same, update the answer.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        dp = [[(-1, -1) for i in range(len(nums))] for j in range(len(nums))]
        ans = 0

        for i in range(len(nums)):
            dp[i][i] = (0, 1) if nums[i] == 1 else (1, 0)
            for j in range(i+1, len(nums)): 
                x, y = dp[i][j-1]
                dp[i][j] = (x, y+1) if nums[j] == 1 else (x+1, y)
                if dp[i][j][0] == dp[i][j][1]:
                    ans = max(ans, j-i+1)  
        return ans
'''

# Optimal solution
# Time: O(N)
# Space: O(N)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # count: A running total. We increment by +1 for 1, and -1 for 0.
        # ans: Keeps track of the maximum subarray length found so far.
        # prefix_map: A dictionary that maps count values to their first occurrence index.
        count = 0
        ans = 0
        # Before we even start looking at the array (i.e., at index -1), the running balance of 1s and 0s is 0, that's why this entry.
        # If I ever hit a balance of 0, that means everything from the beginning till now was balanced.
        prefix_sum = {0: -1}

        for i, num in enumerate(nums):
            # Keep a count of 0s and 1s
            count += 1 if num == 1 else -1
            # If we reach the same count as before eg. if we are at index 5 and our count is 2, but we have seen that count before at index 2, it means array from index 2 to index 5 have same number of 0s and 1s and they summed to 0. So we have an answer there.
            if count in prefix_sum:
                ans = max(ans, i - prefix_sum[count])
            # Add the new count to the dictionary only if one doesn't exist, otherwise we should keep the earlier index as it gives us a longer subarray.
            else:
                prefix_sum[count] = i
        
        return ans
