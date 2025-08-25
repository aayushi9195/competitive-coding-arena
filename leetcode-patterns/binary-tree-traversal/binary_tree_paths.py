# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []

        def dfs(root, path):
            # If we reach a null node, return
            if not root:
                return

            # As we want the output in an arrow separated format
            if path:
                path += "->" + str(root.val)
            else:
                path = str(root.val)

            # If this is a leaf node, we need to update the result by adding the current path and return.
            # We don't need to backtrack i.e. remove node post result updation because path is a string, which means every call maintains its own copy (pass by value).
            if not root.left and not root.right:
                res.append(path)
                return

            # For non-leaf nodes, we need to check for paths both in left and right subtrees.
            dfs(root.left, path)
            dfs(root.right, path)

        # Start with root and keep a track of current path
        dfs(root, "")
        return res
