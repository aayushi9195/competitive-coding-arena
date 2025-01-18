class Solution:

    # Time: O(N)
    # Space: O(N)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        # Contains days in decreasing order of temperature
        stack = []

        for i, t in enumerate(temperatures):
            # If we have reached a warmer temerature than the top of the stack, keep popping and updating the answers for all days whose temperatures are < current day's.
            # Current index - popped index will tells how many days apart the warmer i.e. current day is.
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                result[j] = i - j 

            # Add the current day to stack and wait for a warmer day to come and pop it out.
            stack.append(i)
        
        return result
