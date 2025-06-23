from collections import defaultdict

# Time: O(1) for set() and O(logN) for get()
# Space: O(M*N)
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.store[key]
        l, r  = 0, len(values) - 1
        # We can use binary search because we know the values will always be in the increasing order of timestamps.
        while l <= r:
            m = l + (r - l) // 2
            if values[m][0] > timestamp:
                r = m - 1
            else:
                res = values[m][1]
                l = m + 1
        return res
        
