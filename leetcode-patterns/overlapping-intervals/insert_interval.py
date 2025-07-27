class Solution:
    # Time: O(N)
    # Space: O(N)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):

            # if new interval does not overlap with current interval and comes before it, we can add new interval to the result and return the remaining intervals of the list as it will not overlap with any
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # if new interval does not overlap with current interval and comes after it, we can add current interval to the result but cannot return because new interval may cause overlaps with later intervals
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # new interval overlaps with the current interval, so to merge them take the min start and max end
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # this is to ensure that the new interval is added to result in any case
        # this happens when newInterval overlaps with the last few intervals, or is entirely after all intervals. 
        res.append(newInterval)
        
        return res
