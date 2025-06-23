class Solution:
    # Time: O(mn)
    # Space: O(mn)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        # Start BFS for all rotten oranges; every min all rotten oranges will spoil the ones next to them
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            # Rot applicable oranges at this level
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            # Increment the time once all rotten oranges (popped out from the queue) at this level are processed i.e. they rot the adjacent oranges and put them in the queue.
            time += 1

        # If there are still fresh oranges in the grid, it means we don't have an answer.
        return time if fresh == 0 else -1
