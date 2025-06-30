class Solution:
    # Time: O(N)
    # Space: O(1)
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # As average is always taken of k elements, we will consider the total sum only as max average will be determined by max numerator (denominator will be constant)
        left, right, curr = 0, 0, 0
        # Find the total of the first window
        while right < k:
            curr += nums[right]
            right += 1
        ans = curr

        # Keep sliding the window and updating the current sum to see if we have reached a new maximum
        while right < len(nums):
            curr += nums[right]
            curr -= nums[left]
            right += 1
            left += 1
            ans = max(ans, curr)

        # Finally return the average of max sum window of size k
        return ans/k

        '''
        Pythonic way:
        
        curr = sum(nums[:k])
        max_sum = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr)

        return max_sum / k
        '''
