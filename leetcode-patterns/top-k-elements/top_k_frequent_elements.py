class Solution:
    # Time: O(n + n log k) ≈ O(n log k) -> n to count frequencies, n to build heap, k log n to extract top k
    # Space: O(n) for heap and frequency map
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        # Alternate:
        # from collections import Counter
        # frequencies = Counter(nums)
        
        import heapq
        heap_list = [(-val, key) for key, val in frequencies.items()]
        # This takes linear time O(N) because with in-place heap conversion the height of the tree decreases with every iteration.
        # If we instead do a heappush operation on every element of the list, that would take O(NlogN) time, so this is more efficient. 
        heapq.heapify(heap_list)

        # As we stored frequencies as negative numbers before heapify the list on first element of the tuple i.e. frequencies, the most frequent elements will be on the top of the heap.
        # We remove the min k times to get the k most frequent elements.
        ans = []
        for _ in range(k):
            freq, elem = heapq.heappop(heap_list)
            ans.append(elem)
        
        return ans        
