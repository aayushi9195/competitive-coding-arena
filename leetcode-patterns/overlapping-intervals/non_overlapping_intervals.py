class Solution:
  
    # Time: O(n log n) (due to sorting)
    # Space: O(1) 
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Why Sort by End Time?
        If you sort by end time, you always keep the interval that ends earliest, maximizing space for future intervals — similar to the activity selection problem (greedy).
        Sorting by start time unnecessarily remove more intervals.
        
        Example: intervals = [[1,100], [11,22], [12,25]]
        
        Sorts by start → [[1,100], [11,22], [12,25]]
        Keeps [1,100], skips the other 2 (skip=2)
      
        Optimal:
        Sort by end → [[11,22], [12,25], [1,100]]
        Keep [11,22], skip only 1 (either [12,25] or [1,100]), so skip=1
        '''
        intervals.sort(key=lambda x: x[1])  # sort by end time
        end = float('-inf')
        skip = 0

        for interval in intervals:
            if interval[0] < end:  # overlap
                skip += 1
            else:
                end = interval[1]  # update end to the latest non-overlapping
        return skip     
