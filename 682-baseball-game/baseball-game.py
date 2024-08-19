class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for ope in operations:
            if ope == "C":
                result.pop()
            elif ope == "D":
                result.append(result[-1] * 2)
            elif ope == "+":
                result.append(result[-1] + result[-2])
            else:
                result.append(int(ope))
        return sum(result)
        # time complexity = O(n)
        # space complexity = O(n)