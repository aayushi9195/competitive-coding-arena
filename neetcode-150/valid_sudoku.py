from collections import defaultdict

class Solution:

    # Time: O(N**2)
    # Space: O(N**2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Row/column/square number -> set of numbers from 1-9 already seen
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                # Integer division of rows and cols by 3 gives us the square number i.e. 0-8
                if num in rows[r] or num in cols[c] or num in squares[(r//3, c//3)]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[(r//3, c//3)].add(num)

        return True
        
