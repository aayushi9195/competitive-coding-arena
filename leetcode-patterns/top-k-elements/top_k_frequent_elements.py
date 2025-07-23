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


'''
Alternate approach: Use bucket sort

Bucket Sort Idea:
Count frequencies of each number.
Create a list of buckets, where index i holds a list of numbers that appear exactly i times.
Traverse the buckets in reverse, collecting elements until you have k.


from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        # Step 2: Create buckets; index = frequency
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Step 3: Collect top k frequent elements
        res = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
                    
Time and Space Complexity:
Time: O(n) where n = length of nums (Building frequency map + building buckets + final loop = linear)
Space: O(n) for frequency map + buckets + result
'''
