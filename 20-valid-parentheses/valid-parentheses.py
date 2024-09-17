class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '}': '{',
            ']' : '[',
            ')' : '('
        }
        stack = []
        for char in s:
            if char in hashmap:
                # handle the popping of stack if empty
                popped_ele = stack.pop() if stack else "#"
                if hashmap[char] != popped_ele:
                    return False
            else:
                stack.append(char)
        return not stack
        # time complexity = O(n)
        # space complexity = O(n)