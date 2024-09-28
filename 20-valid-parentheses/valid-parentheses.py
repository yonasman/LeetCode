class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisPair = {
        ']':'[',
        '}' : '{',
        ')' : '('
        }
        stack = []
        for p in s:
            if p not in parenthesisPair:
                stack.append(p)
            else:
                if not stack:
                    return False
                popped_elem = stack.pop()
                if popped_elem != parenthesisPair[p]:
                    return False
        return len(stack) == 0