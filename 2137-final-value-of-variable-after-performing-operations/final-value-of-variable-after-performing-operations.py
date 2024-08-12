class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if operation[1] == "-":
                x -= 1
            else:
                x += 1
        return x
        # time complexity O(n)
        # space complexity O(1)