"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    # Time: O(NlogN + N) = O(NlogN) as we first sort and then iterate over the interval array
    # Space: O(1) or O(N) depending on the sorting algorithm used. Python uses Timsort internally which is a combination of insertion sort and merge sort. For few elements, it uses insertion sort (no extra space needed) but for more elements it uses merge sort (extra space needed).
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # Sort the meetings based on their starting times
        intervals.sort(key = lambda x : x.start)

        # A conflict happens when a meeting is due to start but the previous one has not ended.
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        # Return true if all meetings can be attended without conflict.
        return True 

