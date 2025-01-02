class Solution:

    # Time: O(N)
    # Space: O(N)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Store the counts of all elements i.e. number -> frequency
        counts, n = {}, len(nums)
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Store frequency -> list of elements so that we have elements in their order of frequencies from minimum 1 to maximum N. Using frequency as the index so we have elements in the sorted order.
        # Initialize size N+1 to handle cases where only 1 element is present eg. nums = [1,1,1], so the element 1 will be stored against its frequency i.e. index 3 in the new array.
        frequencies = [[] for _ in range(n + 1)]
        for num, count in counts.items():
            frequencies[count].append(num)

        # Keep getting most frequent elements by traversing in the reverse order until we have k elements.
        i, result = n - 1, []
        while k > 0:
            result.extend(frequencies[i])
            k -= len(frequencies[i])
            i -= 1
        return result

# Note: [[]] * len(nums) - Using this method creates references to the same list object. If you modify one of the lists, all others will reflect the same change.
