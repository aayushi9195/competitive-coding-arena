class Solution:
  
    # Time: O(M*N) as DFS processes each cell only once.
    # Space: O(M*N) as we have recursive calls.
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])

        # Thought process: for every valid cell, we need to count that and then call dfs in all 4 directions to get the counts of sub-islands. Then add them all to get the size of the island at this point.
        # When we encounter any valid cell, we add 1 and continue expanding our island.
        def dfs(i, j):
            # Base condition to stop recursion
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            # So that we don't visit this cell again
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

        for i in range(m):
            for j in range(n):
                # This line is optional but adding this is slighly more efficient as we don't need to trigger DFS for cells that have water.
                if grid[i][j] == 1:
                    # Calculate area at each valid cell.
                    curr_area = dfs(i, j)
                    # Update the max area if found.
                    max_area = max(max_area, curr_area)
        
        return max_area
        
