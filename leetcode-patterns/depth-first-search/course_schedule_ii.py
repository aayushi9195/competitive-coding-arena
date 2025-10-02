from collections import deque, defaultdict
from typing import List

'''
Time: O(V + E)
Space: O(V + E)
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build graph and indegree count
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Create a directed graph using the dependencies given
        for dest, src in prerequisites:
            graph[src].append(dest)
            # indegree[i] stores number of prerequisites course i has.
            indegree[dest] += 1
        
        # Start with all courses having no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for nei in graph[course]:
                # As course is popped, nei has one less prerequisite now.
                indegree[nei] -= 1
                # If nei has no prereqs left, we can pick it up.
                if indegree[nei] == 0:
                    queue.append(nei)
        
        # If we took all courses, return order; else cycle detected
        return order if len(order) == numCourses else []
