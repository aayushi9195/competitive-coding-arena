class Solution:
    # Time: O(N)
    # Space: O(H)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # We can use the recursive inorder traversal too but in that case we need a way to track k across all calls (eg. use self.k instead of k directly as it is passed by value).
        stack = []
        # Iterative inorder traversal
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # When we reach this kth time, we have found the kth smallest element.
            k -= 1
            if k == 0:
                return root.val
            root = root.right
    
