class Solution:

    # Time: O(NlogN)
    # Space: O(N)
    # Main idea: Imagine the cars on a road. Time taken by every car to reach the destination will be the distance left to cover / speed. Cars which are behind can only catch up if the time they need to reach is <= time needed by cars ahead.
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Because a car can only form a fleet with another car that is ahead of it, sorting the array in descending order ensures clarity about the final speed of each car. Sorting in ascending order would create ambiguity, as the next car might form a fleet with another car while reaching the target, making it difficult to determine its final speed.
        # Calculating the time for a car to reach the target is straightforward and can be done using the formula: time = (target - position) / speed. Now, it becomes easy to identify that two cars will form a fleet if and only if the car ahead has a time that is greater than or equal to the time of the car behind it.
        # We can use a stack to maintain the times of the fleets. As we iterate through the array (sorted in descending order of positions), we compute the time for each car to reach the target and check if it can form a fleet with the car ahead. If the current car's time is less than or equal to the top of the stack, it joins the same fleet. Otherwise, it forms a new fleet, and we push its time onto the stack. The length of the stack at the end represents the total number of fleets formed.
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


