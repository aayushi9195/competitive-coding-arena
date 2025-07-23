class Solution:
    # Time: O(NlogK) as we do heap operations push/pop for every element in the array.
    # Space: O(K) as we don't allow the heap to grow beyond K elements.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        # Python by default maintains a minimum heap. 
        # If we limit the size of heap to k - we pop the root i.e. minimum element every time the size of the heap goes beyond k. This means that we will end up having the k largest elements in the heap and the root will be the minimum of those i.e. kth largest element of the array.
        for num in nums:
            heapq.heappush(heap, num) # O(logK) time
            if len(heap) > k:
                heapq.heappop(heap) # O(logK time)
        # Return the kth largest element
        return heap[0]
# Alternate - Quick select (Average case O(N) and worst case O(N2))
