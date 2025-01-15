class Solution:

    # Time: O(N)
    # Space: O(N)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # We can use a stack. We iterate through the array, and if we encounter a number, we push it onto the stack. If we encounter an operator, we pop two elements from the stack, treat them as operands, and solve the equation using the current operator. Then, we push the result back onto the stack.
        # As the array has postfix expression, stack helps us to maintain the correct order of operations by ensuring that we always use the most recent operands (those closest to the operator) when performing the operation. After the iteration, the final result is left in the stack.
        for token in tokens:
            if token == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]
