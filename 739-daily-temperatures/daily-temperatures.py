class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = []
        # iterate over the temps and check the next warmer temp
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                output[index] = i - index
            stack.append(i)
        return output
        # time complexity = O(n)
        # space complexity = O(n)