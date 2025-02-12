class Solution:
    # Time: O(M*N)
    # Space: O(M*N)
    def numIslands(self, grid: List[List[str]]) -> int:
        groups = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        # Do a DFS from every valid start point in all 4 directions and mark 1s as visited because they are all part of the same island.
        # Recursion should stop when we hit the boundaries or if we reach an already visited cell or if the value is not 1.
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] =='0' or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # Pick the start of DFS
        for i in range(m):
            for j in range(n):
                # As each DFS covers 1 island, start of next island will be a cell with value 1 and not visited yet.
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    # No of islands is same as the no of times we need to call DFS.
                    groups += 1
        
        return groups
      
# Note: Space complexity can be reduced by avoiding the visited array. When a cell is visited, we can simply mark it 0 so it is not considered again.

        
