import heapq

class Solution:
  
    # Time: O(k log k) (since at most k elements are in the heap at a time)
    # Space: O(k) for the heap and result list
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
      
        if not nums1 or not nums2:
            return []

        heap = []
        res = []

        # (sum, index in nums1, index in nums2)
        # we use a min-heap to generate only the next most promising pairs (as lists are sorted), starting from: (nums1[0] + nums2[0], (0, 0))
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        # Once the smallest k pairs are added to the heap, we start popping
        # After every pop we push the next promising pair i.e. (i, j+1)
        while heap and len(res) < k:
            total, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

        return res
