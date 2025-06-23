class Solution:
    
    # Time: O(log(m*n))
    # Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Find the row where the result may be found.
        top, down = 0, len(matrix) - 1
        mid = -1
        while top <= down:
            mid = top + (down - top) // 2
            # We got lucky! Target is the first element itself.
            if matrix[mid][0] == target:
                return True
            # If the current row's first element is > target, target will be found in the previous rows.
            if matrix[mid][0] > target:
                down = mid - 1
            # IMP: If the current row's first element is < target, target may either be found in the current row or any row after this.
            else:
                if matrix[mid][-1] >= target:
                    break
                top = mid + 1
        
        # Once the right row is found, perform a usual binary search on it to find the target.
        target_row = mid
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
