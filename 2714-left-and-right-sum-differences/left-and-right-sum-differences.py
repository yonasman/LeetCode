class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        output = []
        for i in range(1,n):
            leftSum[i] = leftSum[i - 1] + nums[i-1]
        for j in range(n - 2,-1,-1):
            rightSum[j] = rightSum[j + 1] + nums[j + 1] 
        for k in range(n):
            output.append(abs(leftSum[k] - rightSum[k]))
        return output