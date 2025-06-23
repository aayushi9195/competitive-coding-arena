from heapq import heapify, heappush, heappop

class Solution:
    # Time: O(NlogN)
    # Space: O(N)
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate the weights so that we have heaviest stones at the root of the minheap.
        heap = [-weight for weight in stones]
        # This taken O(N) time as it uses sift down operations.
        heapify(heap)
        # Keep popping the heaviest stones until we have only one stone remaining.
        while len(heap) > 1:
            # Heappop and heappush take O(logN) time each.
            x, y = -heappop(heap), -heappop(heap)
            # If they are not equal, then push the negation of their absolute difference.
            if x != y:
                heappush(heap, -abs(x - y)) 
        # Handle the edge case where the heap may be empty if all stones are destroyed.
        return -heap[0] if len(heap) == 1 else 0
        
