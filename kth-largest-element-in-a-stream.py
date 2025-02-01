from heapq import heappush, heappop 

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        # Only storing the K largest elements in the heap.
        # As Python heaps are minheap by default, we can use the root element to decide whether the incoming element is a part of K largest elements or not.
        for num in nums:
            if len(self.heap) < k:
                heappush(self.heap, num)
            elif num > self.heap[0]:
                heappop(self.heap)
                heappush(self.heap, num)

    # Time: O(MlogK) where M is the number of times add is called and logK is the time needed each time to get the Kth largest element. Every operation in heap takes logN time.
    # Space: O(K) as we are only storing max K elements in the heap.
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappop(self.heap)
            heappush(self.heap, val)
        return self.heap[0]

'''
Shorter solution: Slightly more time and space complexity as we initialize the heap with all numbers in the array.

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
'''
