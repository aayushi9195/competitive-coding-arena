class Solution:
    # Time: O(M+N)
    # Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # If matrix is empty
        if not matrix or not matrix[0]:
            return False

        r, c = 0, len(matrix[0]) - 1

        # Start from the top right corner. 
        # If it is greater than target, it means we should shift left and look for smaller elements than the current.
        # If it is lesser than target, it means we should shift down and look for greater elements than the current.
        # r is set to 0 and we are always increasing it, so no need to check the lower boundary.
        # c is set to max and we are always decreasing it, so no need to check the higher boundary.
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1

        # If we did not find it
        return False
