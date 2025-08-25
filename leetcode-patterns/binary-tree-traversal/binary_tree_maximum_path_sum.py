# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(N)
    # Space: O(H)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        At every point we need to calculate the value of path without splitting the node and with splitting.
        A valid path cannot have more than one node splitting i.e. considering both left and right subtrees.
        '''
        # we can avoid this global variable to have dfs return two values instead of one - one with splitting and one without splitting
        res = [root.val]

        def dfs(root):

            # to handle null leaf nodes
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # if the nodes are negative, adding them won't increase the path so just exclude them from the current path i.e. mark the value as 0
            leftMax =  max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path value with split to find local maximum
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return the max path value without split to the parent node
            # as we are going to parent, we cannot branch here i.e. only pick left or right and add the root value before going up
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]

        
