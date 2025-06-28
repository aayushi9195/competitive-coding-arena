
# Time: O(N^2)
# Space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # O(NlogN): uses Timsort [Merge Sort (for stability and guaranteed O(n log n)) + Insertion Sort (for small chunks or nearly sorted data)]
        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            # Skip duplicate i values as the triplet with the right j and k is already added
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] + nums[i] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicate j and k values when we find a triplet so that we don't consider the same triplet again
                    while j < k and nums[j] == nums[j-1]: j += 1
                    while j < k and nums[k] == nums[k+1]: k -= 1
                # We don't need to skip duplicate j and k here because we have not found any triplet yet. If we do, we may miss potential triplets. We only care about duplicates when we find triplets.
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1
                else:
                    k -= 1
        
        return triplets
