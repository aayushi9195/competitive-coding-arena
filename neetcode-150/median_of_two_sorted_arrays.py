class Solution:

    # Time: O(log(min(m,n))) because we perform binary search on the smaller array and rest of the operations take constant time.
    # Space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # We want to do binary search on the smaller array.
        if len(nums1) > len(nums2):
            nums1, nums2 =  nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            # We perform binary search on the smaller array and pick the remaining elements from the other array.
            partition1 = (low + high) // 2
            # Size of the first half in merged arrays is m+n/2, and we remove the number of elements taken from the first array, which is partition1.
            # If the total size of merged arrays is odd, we keep the left half > right half by 1.
            partition2 = (m + n + 1) // 2 - partition1

            # Now that we have both partitions i.e. the half that will be considered when we merge the arrays, we need to check if it is a valid half.
            # This can be done by checking that all elements on the left half are <= all elements on the right half.
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]  
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Because the arrays are sorted, we only need to check if max element from left are <= min element from right.
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2:
                    return max(maxLeft1, maxLeft2)
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            
            # Note that we move the pointers only on the smaller array. Because the elements in the other array can be automatically adjusted using total - elements in the first array. In any case, the total elements remain the same, the point is to find out how many elements from each of the arrays will make it to the first half. Depending on the numbers they contain, we need to adjust the partition.
            # This means we are too far on the right side, so move the partition to left.
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            # This means we are too far on the left side, so move the partition to left.
            else:
                low = partition1 + 1
        
        # No valid answer found. This will never happen.
        return -1
              
