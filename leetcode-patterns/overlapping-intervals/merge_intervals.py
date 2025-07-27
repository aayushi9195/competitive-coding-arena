class Solution:
    # Time: O(NlogN)
    # Space: O(N)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sorting takes NlogN time on an average (merge sort + insertion sort i.e. timsort is used)
        intervals.sort(key=lambda x: x[0])

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            # Compare the current interval with the previous interval from the merged list
            # Because if any previous intervals were merged, intervals[i-1] might be outdated
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res
