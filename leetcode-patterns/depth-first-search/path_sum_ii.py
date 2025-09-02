# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Time: O(N) (visit each node once, each path copied only when valid).
    # Space: O(H) for recursion stack + O(N) for storing results (where H = height).
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        self.dfs(root, targetSum, [], ans)
        return ans
    
    def dfs(self, root, targetSum, curr, ans):
        if not root:
            return
        # add current root to the path
        curr.append(root.val)
        # if we reach a leaf node and the target sum, it means we have found a valid path
        if not root.left and not root.right and targetSum == root.val:
            ans.append(list(curr))
        # continue traversing left and right
        self.dfs(root.left, targetSum-root.val, curr, ans)
        self.dfs(root.right, targetSum-root.val, curr, ans)
        # after exploring the root completely, pop out the current root
        curr.pop()
        
        
