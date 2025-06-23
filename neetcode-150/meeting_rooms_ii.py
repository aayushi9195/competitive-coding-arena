"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    # Time: O(NlogN)
    # Space: O(N)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Core idea: Imagine drawing a timeline for all the meetings. We need to check at every timestamp, how many meetings are in progress. Then consider the max across all timestamps. At every point, if a meeting is starting, we increment the count of ongoing meetings. If any meeting is ending, we decrement the count of ongoing meetings. 
        # If a meeting starts at time t and a meeting ends at time t, we end the meeting first because that is not a conflict. 
      
        # Sort all the start and end times
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        days = count = 0
        s = e = 0
        
        while s < len(start):
            # A meeting is due to start but previous has not ended yet
            if start[s] < end[e]:
                count += 1
                s += 1
            # A meeting is due to end 
            else:
                count -= 1
                e += 1
            days = max(count, days)

        return days
            
        
