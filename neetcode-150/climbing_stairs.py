class Solution:
    # Time: O(N)
    # Space: O(N)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # Space can be reduced to O(1) if we maintain only the last two answers at every step as we are only interested in i-1 and i-2, not the whole array.
        steps = [0] * (n+1)
        # Bottom up approach - at every N starting from 1, we see how many ways we can reach that point. Base case is when N=1 and 2. Then onwards, we can use i-1 and i-2 to calculate the total number of ways needed to reach i. This works because we are only allowed to take one or two steps at a time. 
        steps[1], steps[2] = 1, 2
        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]
        # We finally have the total number of ways through which we can reach N.
        return steps[n]

      
