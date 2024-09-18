class Solution:
    def simplifyPath(self, path: str) -> str:
        # a stack to store simplified components
        stack = []
        # split the path to check and simplify the path
        pathComponents = path.split('/')
        # iterate over path components and check each component
        for component in pathComponents:
            # if component is empty or current directory skip
            if component == '' or component == '.':
                continue
            # if the component is the previous directory pop it
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                # otherwise, push the compoent to the stack
                stack.append(component)
        # join starting from / and return the resulting path
        return '/' + '/'.join(stack)
                