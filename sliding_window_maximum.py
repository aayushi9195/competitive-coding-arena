from collections import deque


# Time: O(N)
# Space: O(N)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        l, r = 0, 0
        queue = deque()

        while r < len(nums): 

            # Maintain a decreasing monotonic queue
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
    
            queue.append(r)

            # If the element goes out of window size k, then remove it. Queue will always store the maximum element in the current window.
            if l > queue[0]:
                queue.popleft()

            # From index k onwards, start storing the result. This is the maximum element seen so far in the valid window.
            if r+1 >= k:
                output.append(nums[queue[0]])
                l += 1

            r += 1
        
        return output
