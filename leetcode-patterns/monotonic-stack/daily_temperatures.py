class Solution:
    # Time: O(N)
    # Space: O(N)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        ans = [0 for _ in range(len(temperatures))]  # Alternate: [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # If the current temperature is greater than the top of stack, it means we have found a warmer day for previous days
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i-j
            # While condition ensures that we always insert days in decreasing order of warmness
            stack.append(i)

        return ans
