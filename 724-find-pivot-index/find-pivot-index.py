class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)
        leftSum = 0
        
        for i in range(n):
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1