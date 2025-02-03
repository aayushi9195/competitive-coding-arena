from heapq import heappush, heappop

class Solution:

    # Time: O(nlogk)
    # Space: O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # At any point we only store K points on the heap.
        heap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            # Because python has a min heap by default, we need to manually convert it to max heap.
            # Heap comparison picks the first element in the tuple, and if they are equal it checks other elements from left to right.
            heappush(heap, (-dist, point))
            # As the root element has the max distance from origin so far (as we have negated the distances), we can remove it if the heap size goes beyond k.
            if len(heap) > k:
                heappop(heap)
        # Ignore the distances and return the points only. At this stage we have considered all points in the list 
        return [item[1] for item in heap]
        
        
