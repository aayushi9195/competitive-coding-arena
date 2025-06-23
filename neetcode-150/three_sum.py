class Solution:

    # Time: O(N**2)
    # Space: O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Python uses Timsort (combination of merge sort and insertion sort) by default which uses additional space.
        nums.sort()
        res = []

        # i needs to go till the third last number
        for i in range(len(nums) - 2):

            # skip duplicate i values
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 2-pointer approach
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    
                    # skip duplicates for j and k as we are looking for distinct triplets only
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return res

        
