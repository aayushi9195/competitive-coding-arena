# Time: O(1) for all operations
# Space: O(N) as we need to store minimum for every number.
class MinStack:

    def __init__(self):
        self.stack = []

    # Along with every element, push the minimum element seen so far.
    def push(self, val: int) -> None:
        minimum = min(self.stack[-1][1], val) if self.stack else val
        self.stack.append((val, minimum))        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
