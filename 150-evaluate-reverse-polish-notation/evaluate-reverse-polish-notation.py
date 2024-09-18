class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initialize a stack to track the tokens
        stack = []
        # iterate over the tokens and perform the operation
        for token in tokens:
            if token == '+':
                stack[-2] = stack[-2] + stack[-1]
                stack.pop()
            elif token == '-':
                stack[-2] = stack[-2] - stack[-1]
                stack.pop()
            elif token == '*':
                stack[-2] = stack[-2] * stack[-1]
                stack.pop()
            elif token == '/':
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
            else:
                stack.append(int(token))
        return stack[-1]