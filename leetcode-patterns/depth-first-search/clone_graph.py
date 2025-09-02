"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    # Time: O(N+E) as each edge in the graph is checked at most twice (once from each endpoint in an undirected graph, or once in a directed graph).
    # Space: O(N+E)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {}

        def dfs(node):
            # If a copy of this node is already created, return it
            if node in oldToNew:
                return oldToNew[node]

            # Else create a copy
            copy = Node(node.val)
            oldToNew[node] = copy

            # Copy's neighbors should be same as node's neighbors, so recursively call this function for each of node's neighbors and make them copy's neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            # Once all neighbors are done, return the new node
            return copy


        # Start from the root node
        return dfs(node) if node else None
        
