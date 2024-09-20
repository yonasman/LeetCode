class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for char in s:
            if stack1 and char == "#":
                stack1.pop()
            elif char != '#':
                stack1.append(char)
        for c in t:
            if stack2 and c == "#":
                stack2.pop()
            elif c != '#':
                stack2.append(c)
        return stack1 == stack2
        # time complexity = O(n)
        # space complexity = O(n)