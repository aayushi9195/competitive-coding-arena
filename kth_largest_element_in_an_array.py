from heapq import heapify, heappush, heappop

class Solution:
    # Time: O(N+KlogN) - N to convert nums into heap and then pop K times which takes logN time each.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapify(heap)
        while len(heap) > k:
            heappop(heap)
        return heap[0]

'''
Quick Select Algorithm: 
Works every similar to quick sort. Pick a pivot and partition the array into two halves. As we need the kth largest element, we are looking for element at index len(nums) - k if the array is sorted.
So parition the array, check if the index of pivot element is < or > than the index we want. Look at the left/right half of the array accordingly. If the indices are same, it means pivot is the kth largest. 

# Time: O(n) in average case as we are always discarding one half, O(n^2) in worst case if the pivot selection is bad and leads to skewed distribution of elements around the pivot.
# Space: O(n)
def findKthLargest(self, nums: List[int], k: int) -> int:
      k = len(nums) - k
      
      def quickSelect(l, r):
          pivot, p = nums[r], l
          for i in range(l, r):
              if nums[i] <= pivot:
                  nums[p], nums[i] = nums[i], nums[p]
                  p += 1
          nums[p], nums[r] = nums[r], nums[p]

          if p > k: return quickSelect(l, p - 1)
          elif p < k: return quickSelect(p + 1, r)
          else: return nums[p]

      return quickSelect(0, len(nums) - 1)

'''
