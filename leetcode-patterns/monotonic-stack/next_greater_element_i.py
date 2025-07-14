class Solution:
    # Time: O(M+N)
    # Space: O(N)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        # Stores the next greater element for every element in nums2; defaulting to -1 for answer not found
        next_gt_elems = [-1 for _ in range(len(nums2))]
        # Keeps a track of the positions/numbers we are interested in as we want to return the answer only for the elements present in nums1
        positions = {nums2[i]:i for i in range(len(nums2))}

        # Keep popping from the stack if current element is larger; it means the next greater element for the elements in the stack is found
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                ind = stack.pop()
                next_gt_elems[ind] = nums2[i] 
            # Push to the stack either way; the condition above makes sure all elements on the stack are in decreasing order
            stack.append(i)

        # Return the answer for elements present in nums1 - get the index from positions dict and use that to get the answer from the other array
        ans = [-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            ans[i] = next_gt_elems[positions[nums1[i]]]
        return ans

'''
Shorter version:
Instead of maintaining two data structures for positions/indices and next greater elements, combine them into one dictionary.
Next greater list can store the answer for each number directly instead of each index.

 def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        return [next_greater.get(num, -1) for num in nums1]
'''
