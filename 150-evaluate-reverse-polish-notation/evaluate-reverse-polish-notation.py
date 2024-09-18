class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+','-','*','/'}:
                stack.append(int(token))
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num1 * num2)
                else:
                    if num2 * num1 < 0 and num2 % num1 != 0:
                        stack.append((num2 // num1) + 1)
                    else:
                        stack.append(num2 // num1)
        return stack[-1]